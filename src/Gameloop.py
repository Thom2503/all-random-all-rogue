from typing import List, Optional
from typing_extensions import Self
from Action import Action
from Actor import Actor
from GameResult import GameResult


class Gameloop:
    _actors: List[Actor] = []
    _currentActor: int = 0
    instance: Self

    def addActor(self, actor: Actor) -> None:
        self._actors.append(actor)

    def process(self) -> None:
        if len(self._actors) == 0:
            return
        actor: Actor = self._actors[self._currentActor]
        action: Optional[Action] = actor.getGameAction()
        while action is not None:
            result: GameResult = action.execute()
            if result.alternative is not None:
                action = result.alternative
            if result.succeeded is True:
                self._currentActor: int \
                    = (self._currentActor + 1) % len(self._actors)
