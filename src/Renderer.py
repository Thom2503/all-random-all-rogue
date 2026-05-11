import curses
from typing import List
from Stage import Stage
from Actor import Actor
import Colors


class Renderer:
    def __init__(self, screen):
        self._screen = screen
        curses.curs_set(0)

        curses.init_pair(
            Colors.COLOR_PAIR_FLOOR, curses.COLOR_WHITE, curses.COLOR_BLACK
        )
        curses.init_pair(
            Colors.COLOR_PAIR_WALL, curses.COLOR_WHITE, curses.COLOR_BLACK
        )
        curses.init_pair(
            Colors.COLOR_PAIR_PLAYER, curses.COLOR_YELLOW, curses.COLOR_BLACK
        )

    def render(self, stage: Stage, actors: List[Actor]) -> None:
        self._screen.clear()
        for y in range(stage.height):
            for x in range(stage.width):
                tile = stage.get(x, y)
                try:
                    self._screen.addch(
                        y, x, tile.char, curses.color_pair(tile.color_pair)
                    )
                except curses.error:
                    pass
        for actor in actors:
            try:
                self._screen.addch(
                    actor.y,
                    actor.x,
                    actor.char,
                    curses.color_pair(actor.color_pair)
                )
            except curses.error:
                pass
        self._screen.refresh()
