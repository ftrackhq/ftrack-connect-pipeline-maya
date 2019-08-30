
from ftrack_connect_pipeline.client.publish import QtPipelinePublishWidget
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


class QtPipelineMayaPublishWidget(MayaQWidgetDockableMixin, QtPipelinePublishWidget):
    '''Dockable maya load widget'''
    def __init__(self, event_manager, parent=None):
        # note, we need to pass event_manager as kw as otherwise will complain about double parent argument
        super(QtPipelineMayaPublishWidget, self).__init__(event_manager=event_manager, parent=parent)
        self.setWindowTitle('Maya Pipeline Publisher')

    def show(self):
        super(QtPipelineMayaPublishWidget, self).show(
            dockable=True, floating=False, area='right',
            width=200, height=300, x=300, y=600
    )
