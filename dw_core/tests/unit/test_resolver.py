from dw_core.resolver import ResolutionContext, ResolverRegistry


def test_resolver_registry_builds_kwargs_from_signature():
    class StaticResolver:
        def supports(self, arg_type):
            return arg_type is int

        def resolve(self, *, arg_name, arg_type, context, resolved_kwargs):
            return {arg_name: 123}

    def handler(x: int):
        return x

    registry = ResolverRegistry()
    registry.register(StaticResolver())

    kwargs = registry.resolve_kwargs(handler, ResolutionContext())

    assert kwargs == {'x': 123}
