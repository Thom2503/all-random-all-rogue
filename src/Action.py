from abc import ABC, abstractmethod
from GameResult import GameResult


class Action(ABC):
    @abstractmethod
    def execute(self) -> GameResult:
        pass
