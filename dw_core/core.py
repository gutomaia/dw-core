from importlib.metadata import entry_points

ENTRYPOINT_DOMAIN = 'domain'
ENTRYPOINT_PORTS = 'ports'
ENTRYPOINT_MODULE = 'module'


__all__ = ['get_domain', 'get_ports', 'get_modules']


def get_entrypoints(name):
    return [
        (entrypoint.name, entrypoint.load())
        for entrypoint in entry_points(group=name)
    ]


def get_domain():
    return get_entrypoints(ENTRYPOINT_DOMAIN)


def get_ports():
    return get_entrypoints(ENTRYPOINT_PORTS)


def get_modules():
    return get_entrypoints(ENTRYPOINT_MODULE)
