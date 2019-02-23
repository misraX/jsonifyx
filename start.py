import logging

import urwid

from jsonifyx.config import NAME
from jsonifyx.utils.helpers import line_attr_map, padding_attr_map
from jsonifyx.utils.keys import show_or_exit
from jsonifyx.utils.signals import on_exit_clicked, on_change, on_clear
from jsonifyx.view.constants import PALLETE
from jsonifyx.view.footer import Footer
from jsonifyx.view.header import Header
from jsonifyx.view.input import InputCell
from jsonifyx.view.output import OutputCell

logging.basicConfig(filename=f"{NAME}.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger(NAME)


def main():
    logger.info("############# Program start running.")
    header = padding_attr_map(line_attr_map(urwid.AttrMap(Header(), 'header')))
    footer = padding_attr_map(line_attr_map(urwid.AttrMap(Footer(), 'header')))
    input_text = urwid.Edit("")

    left_cell = InputCell(input_text)

    logger.debug(f"{left_cell.__class__.__name__} editable text: {input_text.text}")

    esc_btn = urwid.Button("Exit")
    clear_btn = urwid.Button("Clear")
    # esc_button = padding_attr_map(urwid.Columns([esc]))

    # input_text = left_cell.input_text()
    output_text = urwid.Text("")

    right_cell = OutputCell(input_widget=input_text, output_text=output_text, callback=on_change)
    btns_col = urwid.Columns([line_attr_map(clear_btn), line_attr_map(esc_btn)])
    grid_flow = padding_attr_map(line_attr_map(
        urwid.GridFlow([line_attr_map(left_cell), line_attr_map(right_cell), btns_col], 100, 0, 0, ('center'))))

    pile = urwid.Pile([
        header,
        grid_flow,
        footer
    ])

    logger.debug(f"Started a pile: {pile.contents}")

    pile = line_attr_map(pile)

    urwid.connect_signal(esc_btn, 'click', on_exit_clicked)
    urwid.connect_signal(clear_btn, 'click', on_clear, weak_args=[input_text])
    loop = urwid.MainLoop(urwid.Filler(pile, 'top'), palette=PALLETE, unhandled_input=show_or_exit)
    logger.debug(f"Started a loop: {loop.widget}")
    loop.run()


if __name__ == '__main__':
    main()
