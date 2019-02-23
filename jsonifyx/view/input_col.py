import logging

import urwid

from jsonifyx.config import NAME

logger = logging.getLogger(NAME)


class InputCell(urwid.Columns):
    """
    Column of pile.
    ---------pile-----------
    |     Header col       |
    |      ----------      |
    |    Line [edit text]  |
    ------------------------
    """

    def __init__(self, editable_text=None):
        if editable_text and not isinstance(editable_text, urwid.Edit):
            raise ValueError(
                f"{self.__class__.__name__} editable_text has to be instance of urwid.Edit but {editable_text} given")
        logger.info(f"{self.__class__.__name__} editable_text is: {editable_text.text}")
        input_text = urwid.Text(self.render_text())
        cel_col = urwid.Pile([input_text, urwid.LineBox(editable_text)])
        super().__init__([cel_col])

    def render_text(self):
        return "Enter your JSON: \n"
