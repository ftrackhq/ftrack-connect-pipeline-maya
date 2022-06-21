# :coding: utf-8
# :copyright: Copyright (c) 2014-2020 ftrack

from ftrack_connect_pipeline_qt.client.asset_manager import (
    QtAssetManagerClientWidget,
)
import ftrack_connect_pipeline.constants as constants
import ftrack_connect_pipeline_qt.constants as qt_constants
import ftrack_connect_pipeline_maya.constants as maya_constants

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from ftrack_connect_pipeline_maya.utils.custom_commands import get_main_window


class MayaQtAssetManagerClientWidget(QtAssetManagerClientWidget):
    def __init__(self, event_manager, asset_list_model, parent=None):
        '''Due to the Maya panel behaviour, we have to use *parent_window*
        instead of *parent*.'''
        super(MayaQtAssetManagerClientWidget, self).__init__(
            event_manager, asset_list_model, parent=get_main_window()
        )


class MayaQtAssetManagerClientWidgetMixin(
    MayaQWidgetDockableMixin, MayaQtAssetManagerClientWidget
):
    ui_types = [
        constants.UI_TYPE,
        qt_constants.UI_TYPE,
        maya_constants.UI_TYPE,
    ]

    '''Dockable maya asset manager widget'''

    def __init__(self, event_manager, asset_list_model):
        super(MayaQtAssetManagerClientWidgetMixin, self).__init__(
            event_manager=event_manager, asset_list_model=asset_list_model
        )
        self.setWindowTitle('ftrack Connect')

    def get_theme_background_style(self):
        return 'maya'

    def show(self):
        super(MayaQtAssetManagerClientWidgetMixin, self).conditional_rebuild()
        super(MayaQtAssetManagerClientWidgetMixin, self).show(
            dockable=True,
            floating=False,
            area='right',
            width=200,
            height=300,
            x=300,
            y=600,
            retain=False,
        )
