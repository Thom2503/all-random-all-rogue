from typing import List
from DefaultTiles import FLOOR, WALL
from Tile import Tile


class Stage:
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
        return self._tiles[y][x]

    def set(self, x: int, y: int, tile: Tile) -> None:
        self._tiles[y][x] = tile

    def inBounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def carveRoom(self, x: int, y: int, w: int, h: int) -> None:
        for ry in range(y, y + h):
            for rx in range(x, x + w):
                self.set(rx, ry, FLOOR)
