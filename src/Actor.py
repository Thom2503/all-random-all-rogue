from abc import ABC, abstractmethod
from typing import Optional
from Action import Action
from Colors import COLOR_PAIR_DEFAULT


class Actor(ABC):
    """
    Abstract class of the actor to be inherited

    Methods:
    setNextAction(self, action) -> None - set the next action to be performed
    getAction(self) -> Optional[Action] - get the action to be performed
    """
    energy: float = 0.0
    speed: float = 1.0
    x: int
    y: int
    char: str = '?'
    color_pair: int = COLOR_PAIR_DEFAULT

    @abstractmethod
    def setNextAction(self, action: Action) -> None:
        """
        Set the next action to be performed

        Parameters:
        self (Self) - this object
        action (Action) - the action that needs to be set next
        """
        pass

    @abstractmethod
    def getAction(self) -> Optional[Action]:
        """
        get the current action that needs to be performed, can be None.

        Parameters:
        self (Self) - this object

        Returns
        action (Optional[Action]) - the action to be performed or None
        """
        pass
