from ftrack_connect_pipeline_qt.client.load import QtPipelineLoaderWidget
from ftrack_connect_pipeline_maya.constants import HOST, UI

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


class QtPipelineMayaLoaderWidget(MayaQWidgetDockableMixin, QtPipelineLoaderWidget):
    '''Dockable maya load widget'''
    def __init__(self, hostid, parent=None):
        super(QtPipelineMayaLoaderWidget, self).__init__(host=HOST, ui=UI, hostid=hostid, parent=parent)
        self.setWindowTitle('Maya Pipeline Loader{}'.format(hostid))

    def show(self):
        super(QtPipelineMayaLoaderWidget, self).show(
            dockable=True, floating=False, area='right',
            width=200, height=300, x=300, y=600
    )
