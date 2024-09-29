from unittest import TestCase

from dw_core.core import get_modules


class EntrypointTest(TestCase):

    def test_len_modules(self):
        self.assertEqual(1, len(get_modules()))

    def test_module_core_name(self):
        name, _ = get_modules()[0]
        self.assertEqual(name, 'dw-core')

    def test_module_core_prog(self):
        _, module = get_modules()[0]
        from dw_core import __prog__

        self.assertEqual(module.__prog__, __prog__)

    def test_module_core_version(self):
        _, module = get_modules()[0]
        from dw_core import __version__

        self.assertEqual(module.__version__, __version__)
