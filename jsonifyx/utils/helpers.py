import urwid

from jsonifyx.config import DEBUG
from jsonifyx.view.constants import PADDING


def line_attr_map(widget):
    """
    Wrap widgets in LineBox.
    TODO: Create a wrapper function to wrap widget rendering.
    :param widget:
    :param line:
    :return:
    """
    if DEBUG:
        widget = urwid.LineBox(widget)
    return widget


def padding_attr_map(widget):
    """
    Default padding.
    TODO: Create a wrapper function to wrap widget rendering.
    :param widget:
    :return:
    """
    return urwid.Padding(widget, align='center', width=('relative', PADDING))
