from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Protocol, get_type_hints


@dataclass(frozen=True)
class ResolutionContext:
    headers: dict[str, str] | None = None
    extras: dict[str, Any] = field(default_factory=dict)


class ArgumentResolver(Protocol):
    def supports(self, arg_type: Any) -> bool:
        raise NotImplementedError()

    def resolve(
        self,
        *,
        arg_name: str,
        arg_type: Any,
        context: ResolutionContext,
        resolved_kwargs: dict[str, Any],
    ) -> dict[str, Any]:
        raise NotImplementedError()


class ResolverRegistry:
    def __init__(self):
        self._resolvers: list[ArgumentResolver] = []

    def register(self, resolver: ArgumentResolver) -> None:
        self._resolvers.append(resolver)

    def resolve_kwargs(
        self,
        func: Callable[..., Any],
        context: ResolutionContext,
    ) -> dict[str, Any]:
        hints = get_type_hints(func)
        resolved: dict[str, Any] = {}

        for arg_name, arg_type in hints.items():
            if arg_name == 'return':
                continue
            for resolver in self._resolvers:
                if resolver.supports(arg_type):
                    resolved.update(
                        resolver.resolve(
                            arg_name=arg_name,
                            arg_type=arg_type,
                            context=context,
                            resolved_kwargs=resolved,
                        )
                    )
                    break

        return resolved
