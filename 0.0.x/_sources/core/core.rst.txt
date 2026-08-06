Core Module
===========

.. module:: dw_core.core

This module provides core functionality for managing entry points in Downwind Core.

Function Overview
-----------------

.. autosummary::
   :toctree: generated
   :nosignatures:

   get_entrypoints
   get_domain
   get_ports
   get_modules

Constants
---------

.. data:: ENTRYPOINT_DOMAIN
   :value: 'domain'

   Entry point group name for domain components.

.. data:: ENTRYPOINT_PORTS
   :value: 'ports'

   Entry point group name for port implementations.

.. data:: ENTRYPOINT_MODULE
   :value: 'module'

   Entry point group name for module extensions.

Detailed Documentation
----------------------

Entry Point Functions
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: get_entrypoints

   Helper function to get entry points for a specific group.

.. autofunction:: get_domain

   Retrieve all registered domain entry points.

.. autofunction:: get_ports

   Retrieve all registered port entry points.

.. autofunction:: get_modules

   Retrieve all registered module entry points.
