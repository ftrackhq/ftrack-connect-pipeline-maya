# :coding: utf-8
# :copyright: Copyright (c) 2014-2020 ftrack

from ftrack_connect_pipeline_qt.client.publish import QtPublisherClient
import ftrack_connect_pipeline.constants as constants
import ftrack_connect_pipeline_qt.constants as qt_constants
import ftrack_connect_pipeline_maya.constants as maya_constants

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


class MayaPublisherClient(MayaQWidgetDockableMixin, QtPublisherClient):
    ui_types = [constants.UI_TYPE, qt_constants.UI_TYPE, maya_constants.UI_TYPE]

    '''Dockable maya load widget'''
    def __init__(self, event_manager, parent=None):
        super(MayaPublisherClient, self).__init__(
            event_manager=event_manager, parent=parent
        )
        self.setWindowTitle('Maya Pipeline Publisher')
        print(self)

    def show(self):
        super(MayaPublisherClient, self).show(
            dockable=True, floating=False, area='right',
            width=200, height=300, x=300, y=600
    )
