from Actor import Actor
from WalkAction import WalkAction
from WaitAction import WaitAction
from Action import Action
from typing import Optional
from Colors import COLOR_PAIR_PLAYER
from Game import Game
from Energy import Energy
from Breed import Breed


class Pienus(Actor):
    """
    The only not random actor next to the player it is a follower and nothing
    more. It's fun :)

    Methods:
    setNextAction(self, action) -> None - the next action
    getPlayer(self, game) -> Optional[Actor] - try to find the player in the
                                               game instance
    canMove(self, game, x, y) -> bool - if Pienus can move to the tile
    getAction(self) -> Optional[Action] - make the moveaction if
                                          that is possible
    """
    _nextAction: Optional[Action] = None
    speed: int = Energy.NORMAL_SPEED
    char: str = 'P'
    color_pair: int = COLOR_PAIR_PLAYER
    game: Game
    breed: Breed
    health: int = 20

    def setNextAction(self, action: Action) -> None:
        """
        Set the next action to be performed

        Parameters:
        self (Self) - this player object
        action (Action) - the action that needs to be set next
        """
        self._nextAction = action

    def getPlayer(self, game: Game) -> Optional[Actor]:
        """
        try to find the player in the game instance to follow the player

        Parameters:
        self (Self) - this object
        game (Game) - the game instance

        Returns:
        actor (Optional[Actor]) - returns the actor iff it is the player
        """
        for actor in game.getActors():
            if actor.char == "@":
                return actor
        return None

    def canMove(self, game: Game, x: int, y: int) -> bool:
        """
        see if pienus can move to the tile

        Parameters:
        self (Self) - this object
        game (Game) - the game object
        x (int) - the x coord
        y (int) - the y coord
        """
        for actor in game.getActors():
            if actor != self and actor.x == x and actor.y == y:
                return False
        return True

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
        player: Optional[Actor] = self.getPlayer(self.game)
        if player is None:
            return WaitAction()

        dx: int = player.x - self.x
        dy: int = player.y - self.y

        def sign(x) -> int:
            return (x > 0) - (x < 0)

        stepX: int = sign(dx)
        stepY: int = sign(dy)

        if dx != 0 and dy != 0:
            if self.canMove(self.game, dx, dy):
                return WalkAction(self, self.game, stepX, stepY)
        if abs(dx) > abs(dy):
            if dx != 0 and self.canMove(self.game, self.x + stepX, self.y):
                return WalkAction(self, self.game, stepX, 0)
        if abs(dy) > abs(dx):
            if dy != 0 and self.canMove(self.game, self.x, self.y + stepY):
                return WalkAction(self, self.game, 0, stepY)

        return WaitAction()