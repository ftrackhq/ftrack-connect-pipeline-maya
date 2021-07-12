# :coding: utf-8
# :copyright: Copyright (c) 2019 ftrack

import os
import logging
import re
from ftrack_connect_pipeline_maya import host as maya_host
from ftrack_connect_pipeline_qt import event
from ftrack_connect_pipeline import constants

import maya.cmds as cmds
import maya.mel as mm
import maya.utils

import ftrack_api

from ftrack_connect_pipeline.configure_logging import configure_logging
extra_handlers = {
    'maya':{
            'class': 'maya.utils.MayaGuiLogHandler',
            'level': 'INFO',
            'formatter': 'file',
        }
}
configure_logging(
    'ftrack_connect_pipeline_maya',
    extra_modules=['ftrack_connect_pipeline', 'ftrack_connect_pipeline_qt'],
    extra_handlers=extra_handlers,
    propagate=False
)


logger = logging.getLogger('ftrack_connect_pipeline_maya')


created_dialogs = dict()

def get_ftrack_menu(menu_name = 'ftrack', submenu_name = 'pipeline'):
    '''Get the current ftrack menu, create it if does not exists.'''
    gMainWindow = mm.eval('$temp1=$gMainWindow')

    if cmds.menu(
            menu_name,
            exists=True,
            parent=gMainWindow,
            label=menu_name
    ):
        menu = menu_name

    else:
        menu = cmds.menu(
            menu_name,
            parent=gMainWindow,
            tearOff=False,
            label=menu_name
        )

    if cmds.menuItem(
            submenu_name,
            exists=True,
            parent=menu,
            label=submenu_name
        ):
            submenu = submenu_name
    else:
        submenu = cmds.menuItem(
            submenu_name,
            subMenu=True,
            label=submenu_name,
            parent=menu
        )

    return submenu

def _open_dialog(dialog_class, event_manager):
    '''Open *dialog_class* and create if not already existing.'''
    dialog_name = dialog_class

    if dialog_name not in created_dialogs:
        ftrack_dialog = dialog_class
        created_dialogs[dialog_name] = ftrack_dialog(
            event_manager
        )

    created_dialogs[dialog_name].show()

def timeline_init():
    '''
    Set the initial framerate with the values set on the shot
    Setup the timeline.
    '''

    # Set FPS

    fps = str(os.getenv('FPS'))

    if not fps is None and 0 < len(fps):

        mapping = {
            '15': 'game',
            '24': 'film',
            '25': 'pal',
            '30': 'ntsc',
            '48': 'show',
            '50': 'palf',
            '60': 'ntscf',
        }

        fps_maya_type = mapping.get(fps, 'pal')
        if not fps_maya_type is None:
            cmds.warning('Setting current unit to {0}'.format(fps))
            cmds.currentUnit(time=fps_maya_type)
        else:
            cmds.warning("Can't translate {} fps to Maya!".format(fps_maya_type))
    else:
        cmds.warning('No fps supplied!')

    # Set animation timeline

    start = os.getenv('FS')
    end = os.getenv('FE')

    if not start is None and 0 < len(start) and not end is None and 0 < len(end):
        start_int = int(float(start))
        end_int = int(float(end))
        cmds.warning('Setting timeline to {0}-{1}'.format(start_int, end_int))
        cmds.playbackOptions(min=start_int, ast=start_int, aet=end_int, max=end_int)



def initialise():
    # TODO : later we need to bring back here all the maya initialiations
    #  from ftrack-connect-maya
    # such as frame start / end etc....

    logger.debug('Setting up the menu')
    session = ftrack_api.Session(auto_connect_event_hub=False)

    event_manager = event.QEventManager(
        session=session, mode=constants.LOCAL_EVENT_MODE
    )

    maya_host.MayaHost(event_manager)

    cmds.loadPlugin('ftrackMayaPlugin.py', quiet=True)

    from ftrack_connect_pipeline_maya.client import load
    from ftrack_connect_pipeline_maya.client import publish
    from ftrack_connect_pipeline_maya.client import asset_manager
    from ftrack_connect_pipeline_maya.client import log_viewer

    # Enable loader and publisher only if is set to run local (default)
    dialogs = []

    dialogs.append(
        (load.MayaLoaderClient, 'Loader')
    )
    dialogs.append(
        (publish.MayaPublisherClient, 'Publisher')
    )
    dialogs.append(
        (asset_manager.MayaAssetManagerClient, 'Asset Manager')
    )
    dialogs.append(
        (log_viewer.MayaLogViewerClient, 'Log Viewer')
    )

    ftrack_menu = get_ftrack_menu()
    # Register and hook the dialog in ftrack menu
    for item in dialogs:
        if item == 'divider':
            cmds.menuItem(divider=True)
            continue

        dialog_class, label = item

        cmds.menuItem(
            parent=ftrack_menu,
            label=label,
            command=(
                lambda x, dialog_class=dialog_class: _open_dialog(dialog_class, event_manager)
            )
        )

    timeline_init()


cmds.evalDeferred('initialise()', lp=True)
