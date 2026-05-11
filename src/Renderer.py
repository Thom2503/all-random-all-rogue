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
                self._screen.addch(y, x, tile.char)

        for actor in actors:
            self._screen.addch(actor.x, actor.y, actor.char)
        self._screen.refresh()
