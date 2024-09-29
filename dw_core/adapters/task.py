from dw_core.adapters.mixins import TaskETAListener, TaskProgressListener
from dw_core.ports import BackgroundTask

__all__ = ['Task']


class Task(BackgroundTask, TaskProgressListener, TaskETAListener):
    def __init__(self):
        super().__init__()
