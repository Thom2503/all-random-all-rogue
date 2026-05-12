from dataclasses import dataclass


@dataclass(frozen=True)
class Tile:
    """
    Dataclass definition of the tile. Nothing else really, only what colour
    needs to be used and if it is walkable. What needs to be printed is in
    char.
    """
    walkable: bool
    char: str
    color_pair: int