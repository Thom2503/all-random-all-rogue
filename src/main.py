import tkinter as tk
from Game import Game
from Renderer import Renderer
from Player import Player
from WalkAction import WalkAction
from Breeds import PIENUS, PLAYER
from Pienus import Pienus
import random

KEYS = {
    "Left":  (-1, 0),
    "Right": (1, 0),
    "Up":    (0, -1),
    "Down":  (0, 1),
}


def main() -> None:
    root = tk.Tk()
    root.title("Roguelike")
    root.configure(bg="black")

    random.seed(42)

    game = Game()
    renderer = Renderer(root, game.stage.width, game.stage.height)

    player = Player()
    (x, y) = game.stage.findOpenTile(game.getActors())
    player.x, player.y = x, y
    player.breed = PLAYER
    game.addActor(player)

    pienus = Pienus()
    pienus.game = game
    pienus.x = player.x - 1
    pienus.y = player.y - 1
    pienus.breed = PIENUS
    game.addActor(pienus)

    def handle_key(event):
        if event.keysym == "q":
            root.destroy()
            return
        if event.keysym in KEYS:
            dx, dy = KEYS[event.keysym]
            player.setNextAction(WalkAction(player, game, dx, dy))
        game.process()
        renderer.render(game.stage, game.getActors())

    root.bind("<Key>", handle_key)

    # Initial render
    game.process()
    renderer.render(game.stage, game.getActors())

    root.mainloop()


if __name__ == "__main__":
    main()
