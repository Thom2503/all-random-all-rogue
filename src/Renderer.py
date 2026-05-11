import curses
from typing import List
from Stage import Stage
from Actor import Actor


class Renderer:
    def __init__(self, screen):
        self._screen = screen
        curses.curs_set(0)

    def render(self, stage: Stage, actors: List[Actor]) -> None:
        self._screen.clear()
        for y in range(stage.height):
            for x in range(stage.width):
                tile = stage.get(x, y)
                try:
                    self._screen.addch(y, x, tile.char)
                except curses.error:
                    pass
        for actor in actors:
            try:
                self._screen.addch(actor.y, actor.x, actor.char)
            except curses.error:
                pass
        self._screen.refresh()
