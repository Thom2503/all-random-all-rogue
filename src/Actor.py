from abc import ABC, abstractmethod
from typing import Optional
from Action import Action
from Colors import COLOR_PAIR_DEFAULT


class Actor(ABC):
    energy: float = 0.0
    speed: float = 1.0
    x: int
    y: int
    char: str = '?'
    color_pair: int = COLOR_PAIR_DEFAULT

    @abstractmethod
    def getAction(self) -> Optional[Action]:
        pass
