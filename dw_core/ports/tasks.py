"""Task interfaces for background processing with progress and ETA tracking.

This module defines interfaces for implementing background tasks that can report
their progress and estimated time of completion. It follows the Observer pattern
for progress and ETA notifications.
"""

from abc import ABCMeta, abstractmethod

__all__ = [
    'TaskProgressCallback',
    'TaskETACallback',
    'TaskProgressListenerInterface',
    'TaskETAListenerInterface',
    'BackgroundTask',
]


class TaskProgressCallback(metaclass=ABCMeta):
    """Interface for receiving task progress updates.

    Implement this interface to receive progress updates from a task.
    Progress is reported as a percentage between 0 and 100.
    """

    @abstractmethod
    def set_progress(self, percentage: float) -> None:
        """Update the progress of a task.

        Args:
            percentage (float): The progress percentage, between 0 and 100.
        """
        pass


class TaskETACallback(metaclass=ABCMeta):
    """Interface for receiving task ETA updates.

    Implement this interface to receive estimated time of arrival (ETA)
    updates from a task.
    """

    @abstractmethod
    def set_eta(self, seconds: float) -> None:
        """Update the estimated time remaining for a task.

        Args:
            seconds (float): Estimated number of seconds remaining until completion.
        """
        pass


class TaskProgressListenerInterface(metaclass=ABCMeta):
    """Interface for managing progress callbacks and updating progress.

    This interface follows the Observer pattern, allowing multiple callbacks
    to be registered for progress updates.
    """

    @abstractmethod
    def add_progress_callback(self, callback: TaskProgressCallback):
        """Register a new progress callback.

        Args:
            callback (TaskProgressCallback): The callback to register.
        """
        pass

    @abstractmethod
    def remove_progress_callback(self, callback: TaskProgressCallback):
        """Unregister a progress callback.

        Args:
            callback (TaskProgressCallback): The callback to unregister.
        """
        pass

    @abstractmethod
    def set_progress(self, percentage: float):
        """Update progress and notify all registered callbacks.

        Args:
            percentage (float): The progress percentage, between 0 and 100.
        """
        pass


class TaskETAListenerInterface(metaclass=ABCMeta):
    """Interface for managing ETA callbacks and updating ETA.

    This interface follows the Observer pattern, allowing multiple callbacks
    to be registered for ETA updates.
    """

    @abstractmethod
    def add_eta_callback(self, callback: TaskETACallback):
        """Register a new ETA callback.

        Args:
            callback (TaskETACallback): The callback to register.
        """
        pass

    @abstractmethod
    def remove_eta_callback(self, callback: TaskETACallback):
        """Unregister an ETA callback.

        Args:
            callback (TaskETACallback): The callback to unregister.
        """
        pass

    @abstractmethod
    def set_eta(self, eta: float):
        """Update ETA and notify all registered callbacks.

        Args:
            eta (float): Estimated number of seconds remaining until completion.
        """
        pass


class BackgroundTask(metaclass=ABCMeta):
    """Base interface for background tasks.

    Implement this interface to create a task that can be run in the background.
    Tasks can optionally implement TaskProgressListenerInterface and/or
    TaskETAListenerInterface to provide progress and ETA updates.
    """

    @abstractmethod
    def run(self):
        """Execute the task.

        This method should contain the main task logic. If the task implements
        progress or ETA interfaces, it should call set_progress() or set_eta()
        at appropriate points during execution.
        """
        pass
