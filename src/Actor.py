from abc import ABC, abstractmethod
from typing import Literal, Optional
from Action import Action
from Colors import COLOR_PAIR_DEFAULT
from Energy import Energy


class Actor(ABC):
    """
    Abstract class of the actor to be inherited

    Methods:
    setNextAction(self, action) -> None - set the next action to be performed
    getAction(self) -> Optional[Action] - get the action to be performed
    needsInput(self) -> Literal[False] - if the actor needs input
    """
    energy: Energy = Energy()
    speed: int = Energy.NORMAL_SPEED
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

    def needsInput(self) -> Literal[False]:
        """
        Determine if the actor needs input or not (i.e. is it a player)

        Parameters:
        self (Self) - this actor

        Returns:
        Literal[False] - by default False
        """
        return False
