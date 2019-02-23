import urwid

from jsonifyx.config import WEBSITE


class Footer(urwid.Columns):

    def __init__(self):
        text = urwid.Text(self.render_text())
        super().__init__([text])

    def render_text(self):
        return f"{WEBSITE}"
