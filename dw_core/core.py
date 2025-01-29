"""Core functionality for managing entry points in Downwind Core.

This module provides functions for discovering and loading entry points that extend
the functionality of Downwind Core. It uses Python's entry points mechanism to
enable a pluggable architecture.
"""

from importlib.metadata import entry_points

ENTRYPOINT_DOMAIN = 'domain'
"""Entry point group name for domain components."""

ENTRYPOINT_PORTS = 'ports'
"""Entry point group name for port implementations."""

ENTRYPOINT_MODULE = 'module'
"""Entry point group name for module extensions."""


__all__ = ['get_domain', 'get_ports', 'get_modules']


def get_entrypoints(name):
    """Retrieve all entry points for a specific group.

    Args:
        name (str): The entry point group name to retrieve.

    Returns:
        list[tuple]: A list of tuples containing (name, loaded_entry_point) pairs.
            The name is the entry point's registered name, and loaded_entry_point
            is the actual loaded object.
    """
    return [
        (entrypoint.name, entrypoint.load())
        for entrypoint in entry_points(group=name)
    ]


def get_domain():
    """Retrieve all registered domain entry points.

    Domain entry points typically provide domain model implementations and
    business logic components.

    Returns:
        list[tuple]: A list of (name, domain_component) pairs.
    """
    return get_entrypoints(ENTRYPOINT_DOMAIN)


def get_ports():
    """Retrieve all registered port entry points.

    Port entry points define interfaces that adapters must implement to
    integrate with the system.

    Returns:
        list[tuple]: A list of (name, port_interface) pairs.
    """
    return get_entrypoints(ENTRYPOINT_PORTS)


def get_modules():
    """Retrieve all registered module entry points.

    Module entry points provide additional functionality or extensions to
    the core system.

    Returns:
        list[tuple]: A list of (name, module_extension) pairs.
    """
    return get_entrypoints(ENTRYPOINT_MODULE)
