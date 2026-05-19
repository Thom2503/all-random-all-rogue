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