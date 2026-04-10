from unittest import TestCase
from unittest.mock import patch

from dw_core.core import get_argument_resolvers


class _FakeEntrypoint:
    def __init__(self, name, obj):
        self.name = name
        self._obj = obj

    def load(self):
        return self._obj


class _AnyResolver:
    def supports(self, arg_type):
        return False

    def resolve(self, *, arg_name, arg_type, context, resolved_kwargs):
        return {}


class ArgumentResolverEntrypointTest(TestCase):
    def test_get_argument_resolvers_instantiates_classes_and_sorts_by_name(self):
        eps = [
            _FakeEntrypoint('b', _AnyResolver),
            _FakeEntrypoint('a', _AnyResolver()),
        ]

        with patch('dw_core.core.entry_points', return_value=eps):
            resolvers = get_argument_resolvers()

        self.assertEqual([name for name, _ in resolvers], ['a', 'b'])
        self.assertFalse(isinstance(resolvers[0][1], type))
        self.assertFalse(isinstance(resolvers[1][1], type))
