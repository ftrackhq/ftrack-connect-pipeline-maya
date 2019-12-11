# :coding: utf-8
# :copyright: Copyright (c) 2019 ftrack

from ftrack_connect_pipeline import constants
from ftrack_connect_pipeline_maya import constants as maya_constants
import maya
from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline_qt import plugin as pluginWidget

class _BaseMaya(plugin._Base):
    host = maya_constants.HOST

    def _run(self, event):
        super_fn = super(_BaseMaya, self)._run
        result = maya.utils.executeInMainThreadWithResult(super_fn, event)
        return result


class BaseMayaPlugin(plugin.BasePlugin, _BaseMaya):
    type = 'plugin'


class BaseMayaWidget(pluginWidget.BasePluginWidget,_BaseMaya):
    type = 'widget'
    ui = maya_constants.UI


class ContextMayaPlugin(BaseMayaPlugin, plugin.ContextPlugin):
    plugin_type = constants.CONTEXT


class ContextMayaWidget(BaseMayaWidget, pluginWidget.ContextWidget):
    plugin_type = constants.CONTEXT


from ftrack_connect_pipeline_maya.plugin.load import *
from ftrack_connect_pipeline_maya.plugin.publish import *