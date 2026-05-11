from abc import ABC, abstractmethod
from typing import Optional
from Action import Action


class Actor(ABC):
    energy: float = 0.0
    speed: float = 1.0
    x: int
    y: int
    char: str = '?'

    @abstractmethod
    def getAction(self) -> Optional[Action]:
        pass
