# :coding: utf-8
# :copyright: Copyright (c) 2016 ftrack

import os
import ftrack_api
import ftrack_connect.application
import logging

logger = logging.getLogger('ftrack_connect_pipeline.listen_maya_launch')

plugin_base_dir = os.path.normpath(
    os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)
        ),
        '..'
    )
)


maya_script_path = os.path.join(
    plugin_base_dir, 'resource', 'maya_plugin'
)

python_dependencies = os.path.join(
    plugin_base_dir, 'dependencies'
)


def on_application_launch(event):
    '''Handle application launch and add environment to *event*.'''

    ftrack_connect.application.appendPath(
        python_dependencies,
        'PYTHONPATH',
        event['data']['options']['env']
    )

    ftrack_connect.application.appendPath(
        maya_script_path,
        'PYTHONPATH',
        event['data']['options']['env']
    )

    event['data']['options']['env']['FTRACK_CONTEXT_ID'] = (
        event['data']['options']['env']['FTRACK_TASKID']
    )


def register(session):
    '''Subscribe to application launch events on *registry*.'''
    if not isinstance(session, ftrack_api.session.Session):
        return

    session.event_hub.subscribe(
        'topic=ftrack.connect.application.launch and data.application.identifier=maya*',
        on_application_launch
    )
