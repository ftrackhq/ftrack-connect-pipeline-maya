# :coding: utf-8
# :copyright: Copyright (c) 2019 ftrack

from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline import constants
from ftrack_connect_pipeline_qt import plugin as pluginWidget
from ftrack_connect_pipeline_maya.plugin import BaseMayaPlugin, BaseMayaWidget


# PLUGINS
class CollectorMayaPlugin(BaseMayaPlugin, plugin.CollectorPlugin):
    plugin_type = constants.COLLECTORS


class ValidatorMayaPlugin(BaseMayaPlugin, plugin.ValidatorPlugin):
    plugin_type = constants.VALIDATORS


class OutputMayaPlugin(BaseMayaPlugin, plugin.OutputPlugin):
    plugin_type = constants.OUTPUTS


class PublisherMayaPlugin(BaseMayaPlugin, plugin.PublisherPlugin):
    plugin_type = constants.PUBLISHERS


# WIDGET
class CollectorMayaWidget(BaseMayaWidget, pluginWidget.CollectorWidget):
    plugin_type = constants.COLLECTORS


class ValidatorMayaWidget(BaseMayaWidget, pluginWidget.ValidatorWidget):
    plugin_type = constants.VALIDATORS


class OutputMayaWidget(BaseMayaWidget, pluginWidget.OutputWidget):
    plugin_type = constants.OUTPUTS


class PublisherMayaWidget(BaseMayaWidget, pluginWidget.PublisherWidget):
    plugin_type = constants.PUBLISHERS
