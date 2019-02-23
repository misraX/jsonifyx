# header
import urwid

from jsonifyx.config import VERSION, NAME


class Header(urwid.Columns):
    """
    Header for program name and version.
    """

    def __init__(self):
        text = urwid.Text(self.render_text())
        super().__init__([text])

    def render_text(self):
        """
        Program name and version.
        """
        return f"{NAME} {VERSION}"
