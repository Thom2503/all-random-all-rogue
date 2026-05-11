from typing import List, Optional
from Actor import Actor
from Action import Action
from ActionResult import ActionResult

ENERGY_THRESHOLD = 1.0
ENERGY_PER_TICK = 1.0


class Game:
    _actors: List[Actor]
    _currentActor: int

    def __init__(self):
        self._actors = []
        self._currentActor = 0

    def process(self) -> None:
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