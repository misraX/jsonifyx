import unittest

import urwid

from jsonifyx.utils.helpers import line_attr_map, padding_attr_map


class HelpersTest(unittest.TestCase):
    def test_line_attr_map(self):
        widget = urwid.Text("Hello")
        wrapped_line = line_attr_map(widget)
        self.assertEqual(type(wrapped_line), urwid.LineBox)

    def test_padding_attr_map(self):
        widget = urwid.Text("Hello")
        wrapped_line = padding_attr_map(widget)
        self.assertEqual(type(wrapped_line), urwid.Padding)
