from typing import List, Optional
from Actor import Actor
from Action import Action
from ActionResult import ActionResult
from Monster import Monster
from Stage import Stage
import random

ENERGY_THRESHOLD = 1.0
ENERGY_PER_TICK = 1.0


class Game:
    """
    The instance of the game itself with the game loop and all the actos
    and stage. Also keeps track of the energy of each actor which is
    dynamic.

    Methods:
    __init__(self) -> None - the constructor where all the actors and stage
                             are initialized
    addActor(self, actor) -> None - add an actor to the game instance
    getActors(self) -> List[Actor] - returns all the actors in this instance
    process(self) -> None - the actual game loop
    """

    _actors: List[Actor]
    _currentActor: int
    stage: Stage

    def __init__(self) -> None:
        self._actors = []
        self._currentActor = 0
        self.stage = Stage(80, 24)
        self.stage.carveRoom()

    def addActor(self, actor: Actor) -> None:
        """
        Add an actor to the game instance, this can be any actor.
        Beware: adding the player again works, but don't do it lol

        Parameters:
        self (Self) - this object
        actor (Actor) - the actor needed to be added
        """
        self._actors.append(actor)

    def getActors(self) -> List[Actor]:
        """
        Get all the actors of the current instance of the game.

        Parameters:
        self (Self) - this object

        Returns:
        List[Actor] - all the actors that are in this instance
        """
        return self._actors

    def process(self) -> None:
        """
        The main game loop where each actor and action is processed. This works
        with the command structure. So each actor has an action to do. Keeps
        track of the energy to keep it kinda dynamic, so some can walk faster
        than others for example.

        Parameters:
        self (Self) - this object instance
        """
        actor = self._actors[self._currentActor]
        actor.energy += actor.speed * ENERGY_PER_TICK

        if actor.energy < ENERGY_THRESHOLD:
            self._currentActor = (self._currentActor + 1) % len(self._actors)
            return

        action: Optional[Action] = actor.getAction()
        if action is None:
            return

        while True:
            result: ActionResult = action.perform()
            if not result.succeeded:
                return
            if result.alternative is None:
                break
            action = result.alternative

        actor.energy -= ENERGY_THRESHOLD
        self._currentActor = (self._currentActor + 1) % len(self._actors)

        self.tryToSpawnMonster()

    def tryToSpawnMonster(self):
        """
        Spawn the monsters in the current stage, but the chance is very low.
        But it is constant meaning that the player has to go on to the next
        level otherwise more and more will be coming.

        Parameters:
        self (Self) - this object
        """
        if random.random() * 100 < 4:
            return
        (x, y) = self.stage.findOpenTile(self.getActors())
        monster = Monster()
        monster.game = self
        monster.x = x
        monster.y = y
        self.addActor(monster)
