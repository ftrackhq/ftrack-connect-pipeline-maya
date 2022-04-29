# :coding: utf-8
# :copyright: Copyright (c) 2014-2020 ftrack

from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline_maya.plugin import BaseMayaPlugin


class AssetManagerActionMayaPlugin(
    plugin.AssetManagerActionPlugin, BaseMayaPlugin
):
    '''
    Class representing a Asset Manager Action Maya Plugin
    '''
