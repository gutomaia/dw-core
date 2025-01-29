"""Task implementation mixins for progress and ETA tracking.

This module provides concrete implementations of the task progress and ETA
listener interfaces. These implementations follow the Observer pattern and
manage lists of callbacks that are notified of updates.
"""

from typing import List

from dw_core.ports import (
    TaskETACallback,
    TaskETAListenerInterface,
    TaskProgressCallback,
    TaskProgressListenerInterface,
)

__all__ = ['TaskProgressListener', 'TaskETAListener']


class TaskProgressListener(TaskProgressListenerInterface):
    """Implementation of TaskProgressListenerInterface.

    This implementation maintains a list of progress callbacks and notifies
    all registered callbacks when progress is updated.

    Example:
        >>> class MyTask(TaskProgressListener):
        ...     def run(self):
        ...         self.set_progress(0)
        ...         # do work
        ...         self.set_progress(50)
        ...         # do more work
        ...         self.set_progress(100)
    """

    def __init__(self):
        """Initialize the progress listener with an empty list of callbacks."""
        super().__init__()
        self.__progress_listeners: List[TaskProgressCallback] = []

    def add_progress_callback(self, callback: TaskProgressCallback):
        """Register a new progress callback.

        Args:
            callback (TaskProgressCallback): The callback to register.
        """
        self.__progress_listeners.append(callback)

    def remove_progress_callback(self, callback: TaskProgressCallback):
        """Unregister a progress callback.

        Args:
            callback (TaskProgressCallback): The callback to unregister.
        """
        if callback in self.__progress_listeners:
            self.__progress_listeners.remove(callback)

    def set_progress(self, percentage: float):
        """Update progress and notify all registered callbacks.

        Args:
            percentage (float): The progress percentage, between 0 and 100.
        """
        if self.__progress_listeners:
            for pl in self.__progress_listeners:
                pl.set_progress(percentage)


class TaskETAListener(TaskETAListenerInterface):
    """Implementation of TaskETAListenerInterface.

    This implementation maintains a list of ETA callbacks and notifies
    all registered callbacks when the ETA is updated.

    Example:
        >>> class MyTask(TaskETAListener):
        ...     def run(self):
        ...         self.set_eta(60)  # 60 seconds remaining
        ...         # do work
        ...         self.set_eta(30)  # 30 seconds remaining
        ...         # do more work
        ...         self.set_eta(0)   # task complete
    """

    def __init__(self):
        """Initialize the ETA listener with an empty list of callbacks."""
        super().__init__()
        self.__eta_listeners: List[TaskETACallback] = []

    def add_eta_callback(self, callback: TaskETACallback):
        """Register a new ETA callback.

        Args:
            callback (TaskETACallback): The callback to register.
        """
        self.__eta_listeners.append(callback)

    def remove_eta_callback(self, callback: TaskETACallback):
        """Unregister an ETA callback.

        Args:
            callback (TaskETACallback): The callback to unregister.
        """
        if callback in self.__eta_listeners:
            self.__eta_listeners.remove(callback)

    def set_eta(self, eta: float):
        """Update ETA and notify all registered callbacks.

        Args:
            eta (float): Estimated number of seconds remaining until completion.
        """
        if self.__eta_listeners:
            for pl in self.__eta_listeners:
                pl.set_eta(eta)
