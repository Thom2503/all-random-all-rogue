import curses
from typing import List
from Stage import Stage
from Actor import Actor
import Colors


class Renderer:
    """
    Object to render the screen in curses. This takes a stage (Stage) object
    and prints the ASCII values of each tile (Tile).

    Methods:
    __init__(self, screen) -> None - constructor also initializes the color
                                     pairs for each tile
    render(self, stage, actors) -> None - the actual renderering in the screen
    """

    def __init__(self, screen) -> None:
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

        curses.init_pair(
            Colors.COLOR_PAIR_MONSTER, curses.COLOR_RED, curses.COLOR_BLACK
        )

    def render(self, stage: Stage, actors: List[Actor]) -> None:
        """
        render the stage and actors to the screen, also colors the tiles based
        on the tile.

        Parameters:
        self (Self) - this object
        stage (Stage) - the stage that needs to be rendered
        actors (List[Actor]) - the actors in this current stage
        """
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
