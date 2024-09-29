from typing import List

from dw_core.ports import (TaskETACallback, TaskETAListenerInterface,
                           TaskProgressCallback, TaskProgressListenerInterface)

__all__ = ['TaskProgressListener', 'TaskETAListener']


class TaskProgressListener(TaskProgressListenerInterface):
    def __init__(self):
        super().__init__()
        self.__progress_listeners: List[TaskProgressCallback] = []

    def add_progress_callback(self, callback: TaskProgressCallback):
        self.__progress_listeners.append(callback)

    def remove_progress_callback(self, callback: TaskProgressCallback):
        if callback in self.__progress_listeners:
            self.__progress_listeners.remove(callback)

    def set_progress(self, percentage: float):
        if self.__progress_listeners:
            for pl in self.__progress_listeners:
                pl.set_progress(percentage)


class TaskETAListener(TaskETAListenerInterface):
    def __init__(self):
        super().__init__()
        self.__eta_listeners: List[TaskETACallback] = []

    def add_eta_callback(self, callback: TaskETACallback):
        self.__eta_listeners.append(callback)

    def remove_eta_callback(self, callback: TaskETACallback):
        if callback in self.__eta_listeners:
            self.__eta_listeners.remove(callback)

    def set_eta(self, eta: float):
        if self.__eta_listeners:
            for pl in self.__eta_listeners:
                pl.set_eta(eta)
