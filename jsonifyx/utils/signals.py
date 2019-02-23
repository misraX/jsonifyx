import logging

import urwid

from jsonifyx.config import NAME
from jsonifyx.utils.jsonify import jsonify

logger = logging.getLogger(NAME)


def on_exit_clicked(button):
    """
    Close on clicked.
    :param button:
    :return:
    """
    raise urwid.ExitMainLoop()


def on_change(input_widget, widget, new_text):
    """
    Event to set the new text for input_widget.
    :param input_widget: Input text widget.
    :param widget:
    :param new_text: New parsed text.
    :return:
    """
    logger.debug(f"Signal fired: {new_text}")
    try:
        new_text = jsonify(new_text)
        logger.info(f"JSONIFY: {new_text}")
        input_widget.set_text(new_text)
    except Exception:
        input_widget.set_text("Bad JSON.")


def on_clear(input_widget, widget):
    logger.debug(f"Signal fired, clearning input. {input_widget.text}")
    input_widget.set_edit_text("")
