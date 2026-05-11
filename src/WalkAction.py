from Action import Action
from ActionResult import ActionResult
from Actor import Actor
from Game import Game


class WalkAction(Action):
    _actor: Actor
    _game: Game
    _dx: int
    _dy: int

    def __init__(self, actor: Actor, game: Game, dx: int, dy: int) -> None:
        self._actor = actor
        self._game = game
        self._dx = dx
        self._dy = dy

    def perform(self) -> ActionResult:
        nx = self._actor.x + self._dx
        ny = self._actor.y + self._dy

        if not self._game.stage.inBounds(nx, ny):
            return ActionResult.failure
        if not self._game.stage.get(nx, ny).walkable:
            return ActionResult.failure

        self._actor.x = nx
        self._actor.y = ny
        return ActionResult.success