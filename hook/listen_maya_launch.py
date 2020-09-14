# :coding: utf-8
# :copyright: Copyright (c) 2016 ftrack

import os
import ftrack_api
import ftrack_connect.application
import logging

logger = logging.getLogger('ftrack_connect_pipeline_maya.listen_maya_launch')

plugin_base_dir = os.path.normpath(
    os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)
        ),
        '..'
    )
)

maya_connect_plugins_path = os.path.join(
    plugin_base_dir, 'resource', 'plug_ins'
)

maya_script_path = os.path.join(
    plugin_base_dir, 'resource', 'scripts'
)

python_dependencies = os.path.join(
    plugin_base_dir, 'dependencies'
)


def on_application_launch(event):
    '''Handle application launch and add environment to *event*.'''

    logger.debug('Adding maya pipeline environments.')

    # Add dependencies in pythonpath
    ftrack_connect.application.prependPath(
        python_dependencies,
        'PYTHONPATH',
        event['data']['options']['env']
    )

    # Maya scripts
    ftrack_connect.application.prependPath(
        maya_script_path,
        'PYTHONPATH',
        event['data']['options']['env']
    )

    ftrack_connect.application.prependPath(
        maya_script_path,
        'MAYA_SCRIPT_PATH',
        event['data']['options']['env']
    )

    # Maya plugins
    ftrack_connect.application.prependPath(
        maya_connect_plugins_path,
        'MAYA_PLUG_IN_PATH',
        event['data']['options']['env']
    )

    # Discover plugins from definitions
    definitions_plugin_hook = event['data']['options']['env'].get(
        'FTRACK_DEFINITION_PLUGIN_PATH'
    )
    plugin_hook = os.path.join(definitions_plugin_hook, 'maya')
    # Add plugins to events path.
    ftrack_connect.application.appendPath(
        plugin_hook,
        'FTRACK_EVENT_PLUGIN_PATH',
        event['data']['options']['env']
    )


def register(session):
    '''Subscribe to application launch events on *registry*.'''
    if not isinstance(session, ftrack_api.session.Session):
        return

    session.event_hub.subscribe(
        'topic=ftrack.connect.application.launch and '
        'data.application.identifier=maya*',
        on_application_launch, priority=40
    )
