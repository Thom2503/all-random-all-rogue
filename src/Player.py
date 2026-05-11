from typing import Optional
from Action import Action
from Actor import Actor
from Colors import COLOR_PAIR_PLAYER


class Player(Actor):
    _nextAction: Optional[Action] = None
    speed: float = 1.0
    char: str = '@'
    color_pair: int = COLOR_PAIR_PLAYER

    def setNextAction(self, action: Action) -> None:
        self._nextAction = action

    def getAction(self) -> Optional[Action]:
        action: Optional[Action] = self._nextAction
        self._nextAction = None
        return action
