from ftrack_connect_pipeline.client.load import QtPipelineLoaderWidget
from ftrack_connect_pipeline_maya.constants import HOST, UI

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


class QtPipelineMayaLoaderWidget(MayaQWidgetDockableMixin, QtPipelineLoaderWidget):
    '''Dockable maya load widget'''
    def __init__(self, event_manager, parent=None):
        super(QtPipelineMayaLoaderWidget, self).__init__(event_manager=event_manager, parent=parent)
        self.setWindowTitle('Maya Pipeline Loader {}'.format(event_manager.hostid))

    def show(self):
        super(QtPipelineMayaLoaderWidget, self).show(
            dockable=True, floating=False, area='right',
            width=200, height=300, x=300, y=600
    )
