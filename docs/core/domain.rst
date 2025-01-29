Domain Module
=============

.. module:: dw_core.domain

This module provides domain-specific command responses.

Class Overview
--------------

.. autosummary::
   :toctree: generated
   :nosignatures:

   CommandAccept
   CommandExecuted

Detailed Documentation
----------------------

Command Response Classes
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: CommandAccept
   :members:
   :show-inheritance:

   Represents a response indicating command acceptance (HTTP 202).

.. autoclass:: CommandExecuted
   :members:
   :show-inheritance:

   Represents a response indicating command execution (HTTP 200).
