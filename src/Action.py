from abc import ABC, abstractmethod
from ActionResult import ActionResult


class Action(ABC):
    @abstractmethod
    def perform(self) -> ActionResult:
        pass
