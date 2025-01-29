"""Task implementation combining progress and ETA tracking.

This module provides a concrete Task class that implements both progress
and ETA tracking capabilities.
"""

from dw_core.adapters.mixins import TaskETAListener, TaskProgressListener
from dw_core.ports import BackgroundTask

__all__ = ['Task']


class Task(BackgroundTask, TaskProgressListener, TaskETAListener):
    """Base class for background tasks with progress and ETA tracking.

    This class combines the BackgroundTask interface with progress and ETA
    tracking capabilities. Subclasses should implement the run() method
    and use set_progress() and set_eta() to provide updates during execution.

    Example:
        >>> class MyTask(Task):
        ...     def run(self):
        ...         self.set_progress(0)
        ...         self.set_eta(60)
        ...         # do work
        ...         self.set_progress(50)
        ...         self.set_eta(30)
        ...         # do more work
        ...         self.set_progress(100)
        ...         self.set_eta(0)
    """

    def __init__(self):
        """Initialize the task with progress and ETA tracking capabilities."""
        super().__init__()
