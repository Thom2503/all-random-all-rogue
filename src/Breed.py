from typing import Set, Any, List
from Attack import Attack
from Use import Use


class Breed:
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