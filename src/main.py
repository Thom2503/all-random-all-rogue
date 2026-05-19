from Game import Game
from Pienus import Pienus
from Renderer import Renderer
from Player import Player
import curses
from WalkAction import WalkAction
import random

KEYS = {
    curses.KEY_LEFT: (-1, 0),
    curses.KEY_RIGHT: (1, 0),
    curses.KEY_UP: (0, -1),
    curses.KEY_DOWN: (0, 1),
}


def main(screen) -> None:
    """
    Main function here input is taken from the screen and the player is
    instanced

    Parameters:
    screen (?) - the screen to be rendered to
    """
    game: Game = Game()
    renderer: Renderer = Renderer(screen)
    random.seed(42)

    player: Player = Player()
    (x, y) = game.stage.findOpenTile(game.getActors())
    player.x = x
    player.y = y
    game.addActor(player)

    pienus: Pienus = Pienus()
    pienus.game = game
    pienus.x = player.x - 1
    pienus.y = player.y - 1
    game.addActor(pienus)

    while True:
        renderer.render(game.stage, game.getActors())
        game.process()
        key = screen.getch()
        if key == ord('q'):
            break
        if key in KEYS:
            dx, dy = KEYS[key]
            player.setNextAction(WalkAction(player, game, dx, dy))


if __name__ == "__main__":
    curses.wrapper(main)
