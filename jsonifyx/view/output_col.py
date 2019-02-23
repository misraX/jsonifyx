import logging

import urwid

from jsonifyx.config import NAME

logger = logging.getLogger(NAME)


class OutputCell(urwid.Columns):
    """
    Column of pile.
    ---------pile-----------
    |     Header col       |
    |      ----------      |
    |    Line [outpt text] |
    ------------------------
    """

    def __init__(self, input_widget, output_text=None, callback=None):
        input_text = urwid.Text(self.render_text())

        logger.info(f"{self.__class__.__name__} input_text: {input_text.text}")
        logger.info(f"{self.__class__.__name__} input: {input_widget.text}")

        urwid.connect_signal(input_widget, 'change', callback, weak_args=[output_text])
        logger.debug(f"Your Output text is: {output_text.text}")
        cel_col = urwid.Pile([input_text, urwid.LineBox(output_text)])
        super().__init__([cel_col])

    def render_text(self):
        return "Your JSON output: \n"
