CQRS Module
===========

.. module:: dw_core.cqrs

This module provides the base classes for implementing CQRS pattern.

Class Overview
--------------

.. autosummary::
   :toctree: generated
   :nosignatures:

   CQRSRequest
   CQRSResponse
   Command
   Query
   Event

Detailed Documentation
----------------------

Base Request/Response Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: CQRSRequest
   :members:
   :show-inheritance:

.. autoclass:: CQRSResponse
   :members:
   :show-inheritance:

CQRS Pattern Classes
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: Command
   :members:
   :show-inheritance:

.. autoclass:: Query
   :members:
   :show-inheritance:

.. autoclass:: Event
   :members:
   :show-inheritance:
