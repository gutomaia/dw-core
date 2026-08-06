Tasks Module
============

.. module:: dw_core.ports.tasks

This module provides interfaces and base classes for implementing background tasks with progress and ETA tracking capabilities.

Interface Overview
----------------

.. autosummary::
   :toctree: generated
   :nosignatures:

   TaskProgressCallback
   TaskETACallback
   TaskProgressListenerInterface
   TaskETAListenerInterface
   BackgroundTask

Implementation Overview
---------------------

.. currentmodule:: dw_core.adapters.mixins

.. autosummary::
   :toctree: generated
   :nosignatures:

   TaskProgressListener
   TaskETAListener

.. currentmodule:: dw_core.adapters.task

.. autosummary::
   :toctree: generated
   :nosignatures:

   Task

Detailed Documentation
--------------------

Task Interfaces
~~~~~~~~~~~~~

.. currentmodule:: dw_core.ports.tasks

.. autoclass:: TaskProgressCallback
   :members:
   :show-inheritance:

   Interface for receiving task progress updates.

.. autoclass:: TaskETACallback
   :members:
   :show-inheritance:

   Interface for receiving task ETA (Estimated Time of Arrival) updates.

.. autoclass:: TaskProgressListenerInterface
   :members:
   :show-inheritance:

   Interface for managing progress callbacks and updating progress.

.. autoclass:: TaskETAListenerInterface
   :members:
   :show-inheritance:

   Interface for managing ETA callbacks and updating ETA.

.. autoclass:: BackgroundTask
   :members:
   :show-inheritance:

   Base interface for background tasks.

Task Implementations
~~~~~~~~~~~~~~~~~

.. currentmodule:: dw_core.adapters.mixins

.. autoclass:: TaskProgressListener
   :members:
   :show-inheritance:

   Implementation of TaskProgressListenerInterface that manages a list of progress callbacks.

.. autoclass:: TaskETAListener
   :members:
   :show-inheritance:

   Implementation of TaskETAListenerInterface that manages a list of ETA callbacks.

.. currentmodule:: dw_core.adapters.task

.. autoclass:: Task
   :members:
   :show-inheritance:

   Concrete implementation of a background task that supports both progress and ETA tracking.
