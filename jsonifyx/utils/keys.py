import urwid


def show_or_exit(key):
    """
    Exit the main loop on 'q'.
    :param key:
    :return:
    """
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
