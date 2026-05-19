from __future__ import annotations
from Action import Action
from ActionResult import ActionResult
from Actor import Actor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Game import Game


class WalkAction(Action):
    """
    The walk action. This action makes the player, NPC, walls whatever you want
    walkable.

    Methods:
    __init__(self, actor, game, dx, dy) -> None - constructor
    perform(self) -> ActionResult - the actual action to be performed
    """
    _actor: Actor
    _game: Game
    _dx: int
    _dy: int

    def __init__(self, actor: Actor, game: Game, dx: int, dy: int) -> None:
        self._actor: Actor = actor
        self._game: Game = game
        self._dx: int = dx
        self._dy: int = dy

    def perform(self) -> ActionResult:
        """
        Walk to the dx and dy difference. If the action is not possible return
        the failure otherwise return success.
        """
        nx: int = self._actor.x + self._dx
        ny: int = self._actor.y + self._dy

        for actor in self._game.getActors():
            if actor.x == nx and \
               actor.y == ny and \
               actor.breed.name != "pienus":
                # to avoid more circular imports import it here...
                from AttackAction import AttackAction
                if self._actor.breed.name != "pienus":
                    return ActionResult.alternate(
                        AttackAction(self._actor, actor, self._game)
                    )

        if not self._game.stage.inBounds(nx, ny):
            return ActionResult.failure
        if not self._game.stage.get(nx, ny).walkable:
            return ActionResult.failure

        self._actor.x = nx
        self._actor.y = ny
        return ActionResult.success