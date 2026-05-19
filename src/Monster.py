from Actor import Actor
from Action import Action
from Colors import COLOR_PAIR_MONSTER
from typing import Any, Optional
from WaitAction import WaitAction
from WalkAction import WalkAction
from Breed import Breed
from Energy import Energy
from Attack import Attack
import random


class Monster(Actor):
    """
    This is the base monster class all the monsters are ultimatly this

    Methods:
    setNextAction(self, action) -> None - what the next action should be
    getAction(self) -> Optional[Action] - what action needs to be performed now
    """
    _nextAction: Optional[Action] = None
    char: str = 'M'
    color_pair: int = COLOR_PAIR_MONSTER
    game: Any
    breed: Breed
    speed: int
    health: int = 5

    def __init__(self, breed: Optional[Breed] = None) -> None:
        super().__init__()
        if breed is None:
            self.breed = Breed(
                name="monster",
                app="M",
                speed=0,
                max_hp=5,
                attack=Attack(1, 2, 60, "scratch"),
                defence=5,
                hit_chance=65,
                canOpenDoors=False,
                moves=[],
                flags=set(),
            )
        else:
            self.breed = breed
        self.speed: int = min(
            Energy.MAX_SPEED,
            max(Energy.MIN_SPEED, Energy.NORMAL_SPEED + self.breed.speed)
        )

    def setNextAction(self, action: Action) -> None:
        """
        Set the next action to be performed

        Parameters:
        self (Self) - this monster object
        action (Action) - the action that needs to be set next
        """
        self._nextAction = action

    def getAction(self) -> Optional[Action]:
        """
        get the current action that needs to be performed, either walk or wait
        action for now. the goal is to follow the player that is set in the
        game instance.

        Parameters:
        self (Self) - this player object

        Returns
        action (Optional[Action]) - the action to be performed or None
        """
        directions = [
            (-1, -1), (0, -1), (1, -1),
            (-1,  0),          (1,  0),
            (-1,  1), (0,  1), (1,  1),
        ]

        if random.random() < 0.2:
            return WaitAction()

        dx, dy = random.choice(directions)

        return WalkAction(self, self.game, dx, dy)