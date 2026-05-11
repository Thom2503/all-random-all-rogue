from Colour import Colour
from Action import Action
from typing import Optional


class Actor:
    nextAction: Optional[Action]

    def __init__(self, x: int, y: int, char: str, colour: Colour) -> None:
        self.x = x
        self.y = y
        self.char = char
        self.colour = colour

    def setPosition(self, game, to) -> None:
        pass

    def getGameAction(self) -> Optional[Action]:
        action: Optional[Action] = self.nextAction
        self.nextAction = None
        return action
