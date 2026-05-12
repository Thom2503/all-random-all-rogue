from Actor import Actor
from Action import Action
from Colors import COLOR_PAIR_MONSTER
from typing import Optional

from WaitAction import WaitAction


class Monster(Actor):
    """
    This is the base monster class all the monsters are ultimatly this

    Methods:
    setNextAction(self, action) -> None - what the next action should be
    getAction(self) -> Optional[Action] - what action needs to be performed now
    """
    _nextAction: Optional[Action] = None
    energy: float = 2.0
    speed: float = 1.0
    char: str = 'M'
    color_pair: int = COLOR_PAIR_MONSTER

    def setNextAction(self, action: Action) -> None:
        """
        Set the next action to be performed

        Parameters:
        self (Self) - this player object
        action (Action) - the action that needs to be set next
        """
        self._nextAction = action

    def getAction(self) -> Optional[Action]:
        """
        get the current action that needs to be performed, can be None.

        Parameters:
        self (Self) - this monster object

        Returns
        action (Optional[Action]) - the action to be performed or None
        """
        return WaitAction()