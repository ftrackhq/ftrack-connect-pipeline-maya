# :coding: utf-8
# :copyright: Copyright (c) 2014-2020 ftrack

import tempfile

import maya.cmds as cmd
import maya

from ftrack_connect_pipeline_maya import plugin
import ftrack_api



class OutputMayaAlembicPlugin(plugin.PublisherOutputMayaPlugin):

    plugin_name = 'alembic'

    def extract_options(self, options):

        return {
            'alembicAnimation' : bool(options.get('alembicAnimation', True)),
            'frameStart': float(
                options.get('frameStart', cmd.playbackOptions(q=True, ast=True))
            ),
            'frameEnd': float(
                options.get('frameEnd', cmd.playbackOptions(q=True, aet=True))
            ),
            'alembicUvwrite': bool(options.get('alembicUvwrite', True)),
            'alembicWorldspace': bool(options.get('alembicWorldspace', False)),
            'alembicWritevisibility': bool(options.get('alembicWritevisibility', False)),
            'alembicEval': float(options.get('alembicEval', 1.0))
        }

    def run(self, context=None, data=None, options=None):
        # ensure to load the alembic plugin
        cmd.loadPlugin('AbcExport.so', qt=1)

        component_name = options['component_name']
        new_file_path = tempfile.NamedTemporaryFile(
            delete=False,
            suffix='.abc'
        ).name

        options = self.extract_options(options)

        self.logger.debug(
            'Calling output options: data {}. options {}'.format(
                data, options
            )
        )

        cmd.select(data, r=True)
        selectednodes = cmd.ls(sl=True, long=True)
        nodes = cmd.ls(selectednodes, type='transform', long=True)

        objCommand = ''
        for n in nodes:
            objCommand = objCommand + '-root ' + n + ' '

        alembicJobArgs = []

        if options.get('alembicUvwrite'):
            alembicJobArgs.append('-uvWrite')

        if options.get('alembicWorldspace'):
            alembicJobArgs.append('-worldSpace')

        if options.get('alembicWritevisibility'):
            alembicJobArgs.append('-writeVisibility')

        if options.get('alembicAnimation'):
            alembicJobArgs.append(
                '-frameRange {0} {1} -step {2} '.format(
                    options['frameStart'],
                    options['frameEnd'],
                    options['alembicEval']
                )
            )

        alembicJobArgs = ' '.join(alembicJobArgs)
        alembicJobArgs += ' ' + objCommand + '-file ' + new_file_path
        cmd.AbcExport(j=alembicJobArgs)

        if selectednodes:
            cmd.select(selectednodes)

        return {component_name: new_file_path}


def register(api_object, **kw):
    if not isinstance(api_object, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return
    ma_plugin = OutputMayaAlembicPlugin(api_object)
    ma_plugin.register()
