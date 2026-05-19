from typing import List, Set
from Attack import Attack
from dataclasses import dataclass
from Use import Use


@dataclass
class Breed:
    """
    Breed class to have some more dynamic NPCs, with all kinds of different
    mechanics and attributs. This class makes the Hierarchy wide not deep.
    """
    name: str
    app: str
    speed: int
    max_hp: int
    attack: Attack
    defence: int
    hit_chance: int
    canOpenDoors: bool
    moves: List[Use]
    flags: Set[str]