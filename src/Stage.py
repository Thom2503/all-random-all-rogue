from typing import List
from CellularAutomata import CellularAutomata
from DefaultTiles import FLOOR, WALL
from Tile import Tile


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

    def carveRoom(self, x: int, y: int, w: int, h: int) -> None:
        """
        Carve the room out in the stage.
        TODO: I want to add like cellular automata or something

        Parameters:
        self (Self) - this object
        x (int) - where the room needs to begin
        y (int) - where the room needs to begin
        w (int) - how wide the room needs to be
        h (int) - how high the room needs to be
        """
        CellularAutomata.fillStage(self, self.width, self.height)
