from typing import List, Tuple, Optional
from CellularAutomata import CellularAutomata
from DefaultTiles import WALL, FLOOR
from Tile import Tile
from Actor import Actor
import random


class Stage:
    """
    The current stage to display, so it is a matrix of tiles that ought to be
    displayed to the player.

    Methods:
    __init__(self, width, height) -> None - constructor of the stage
    get(self, x, y) -> Tile - what tile is at the x and y place
    set(self, x, y, tile) -> None - set a tile at that x and y place
    inBounds(self, x, y) -> bool - if the player or object is in the bounds
                                   of the stage
    carveRoom(self, x, y, w, h) -> None - make the actual room.
    """

    width: int
    height: int
    _tiles: List[List[Tile]]

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._tiles = [
            [WALL for _ in range(width)]
            for _ in range(height)
        ]

    def get(self, x: int, y: int) -> Tile:
        """
        get the tile at that x and y point in the stage.

        Parameters:
        self (Self) - this object
        x (int) - the x coord
        y (int) - the y coord

        Returns:
        Tile - the tile that is found
        """
        return self._tiles[y][x]

    def set(self, x: int, y: int, tile: Tile) -> None:
        """
        set the tile at the point of the x and y coordinates.

        Parameters:
        self (Self) - this object
        x (int) - the x coord
        y (int) - the y coord
        tile (Tile) - what tile that needs to be placed
        """
        self._tiles[y][x] = tile

    def inBounds(self, x: int, y: int) -> bool:
        """
        Check if the actor or tile is in the bounds of the stage.

        Parameters:
        self (Self) - this stage object
        x (int) - the x coord
        y (int) - the y coord

        Returns:
        bool - if the object is in bounds of the stage
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def carveRoom(self) -> None:
        """
        Carve the room out in the stage.
        TODO: I want to add like cellular automata or something

        Parameters:
        self (Self) - this object
        """
        CellularAutomata.fillStage(self, self.width, self.height, 30)

    def actorAt(
        self,
        pos: Tuple[int, int],
        actors: List[Actor]
    ) -> Optional[Actor]:
        """
        check if an actor is at the position x and y and return that actor, if
        not found then None is returned.

        Parameters:
        self (Self) - this object
        pos (Tuple[int, int]) - x and y position
        actors (List[Actor]) - the actors in the game now

        Returns:
        actor (Optional[Actor]) - returns the actor if found
        """
        x, y = pos
        for actor in actors:
            if actor.x == x and actor.y == y:
                return actor
        return None

    def findOpenTile(self, actors: List[Actor]) -> Tuple[int, int]:
        """
        Find a tile that the actor can be placed on.

        Parameters:
        self (Self) - this object
        actors (List[Actor]) - the list of all the actors

        Returns:
        (x, y) (Tuple[int, int]) - the x and y coords
        """
        while True:
            x: int = random.randrange(self.width)
            y: int = random.randrange(self.height)
            tile: Tile = self.get(x, y)
            if not tile.walkable:
                continue
            if self.actorAt((x, y), actors) is not None:
                continue
            return (x, y)
