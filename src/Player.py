from typing import Optional
from Action import Action
from Actor import Actor
from Colors import COLOR_PAIR_PLAYER
from Energy import Energy


class Player(Actor):
    """
    Player class this is the actual user

    Methods:
    setNextAction(self, action) -> None - what the next action should be
    getAction(self) -> Optional[Action] - what action needs to be performed now
    """
    _nextAction: Optional[Action] = None
    speed: int = Energy.NORMAL_SPEED
    char: str = '@'
    color_pair: int = COLOR_PAIR_PLAYER

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
        self (Self) - this player object

        Returns
        action (Optional[Action]) - the action to be performed or None
        """
        action: Optional[Action] = self._nextAction
        self._nextAction = None
        return action

    def needsInput(self) -> bool:
        return self._nextAction is None
