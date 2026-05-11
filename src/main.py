from typing import NoReturn
from Game import Game
from Renderer import Renderer
from Player import Player
import curses


def main(screen) -> NoReturn:
    game: Game = Game()
    renderer: Renderer = Renderer(screen)

    player: Player = Player()
    player.x, player.y = 2, 2
    game.addActor(player)

    while True:
        renderer.render(game.stage, game.getActors())
        game.process()


if __name__ == "__main__":
    curses.wrapper(main)
