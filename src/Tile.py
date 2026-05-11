from dataclasses import dataclass


@dataclass(frozen=True)
class Tile:
    walkable: bool
    char: str