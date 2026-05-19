from typing import Set, Any, List
from Attack import Attack
from Use import Use


class Breed:
    """
    Breed class to have some more dynamic NPCs, with all kinds of different
    mechanics and attributs. This class makes the Hierarchy wide not deep.
    """
    name: str
    maxHealth: int
    attack: Attack
    moves: List[Use]
    flags: Set[str]
    loot: Any
    speed: int
    canOpenDoors: bool
    app: str

    def __init__(self, speed: int, app: str, canOpenDoors: bool) -> None:
        self.speed = speed
        self.appearance = app
        self.canOpenDoors = canOpenDoors