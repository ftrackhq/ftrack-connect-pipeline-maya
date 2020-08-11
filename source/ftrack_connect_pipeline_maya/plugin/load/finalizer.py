# :coding: utf-8
# :copyright: Copyright (c) 2019 ftrack

from ftrack_connect_pipeline import plugin
from ftrack_connect_pipeline_qt import plugin as pluginWidget
from ftrack_connect_pipeline_maya.plugin import (
    BaseMayaPlugin, BaseMayaPluginWidget
)


class LoaderFinalizerMayaPlugin(plugin.LoaderFinalizerPlugin, BaseMayaPlugin):
    ''' Class representing a Finalizer Plugin

        .. note::

            _required_output is a dictionary containing the 'context_id',
            'asset_name', 'asset_type', 'comment' and 'status_id' of the
            current asset
    '''


class LoaderFinalizerMayaWidget(
    pluginWidget.LoaderFinalizerWidget, BaseMayaPluginWidget
):
    ''' Class representing a Finalizer Widget

        .. note::

            _required_output is a dictionary containing the 'context_id',
            'asset_name', 'asset_type', 'comment' and 'status_id' of the
            current asset
    '''