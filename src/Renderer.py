import tkinter as tk
from typing import List
from Stage import Stage
from Actor import Actor
from Colors import (
    COLOR_PAIR_FLOOR,
    COLOR_PAIR_MONSTER,
    COLOR_PAIR_PLAYER,
    COLOR_PAIR_WALL
)

CELL_W = 10
CELL_H = 18
FONT = ("Courier", 14)

COLOR_MAP = {
    COLOR_PAIR_FLOOR: ("white", "black"),   # floor
    COLOR_PAIR_WALL: ("white", "black"),   # wall
    COLOR_PAIR_PLAYER: ("yellow", "black"),   # player
    COLOR_PAIR_MONSTER: ("red", "black"),   # monster
}


class Renderer:

    def __init__(self, root, stage_width: int, stage_height: int) -> None:
        canvas_w = stage_width * CELL_W
        canvas_h = (stage_height + 3) * CELL_H

        self._canvas = tk.Canvas(
            root,
            width=canvas_w,
            height=canvas_h,
            bg="black",
            highlightthickness=0,
        )
        self._canvas.pack()

    def _draw_char(self, x: int, y: int, char: str, color: str) -> None:
        px = x * CELL_W + CELL_W // 2
        py = y * CELL_H + CELL_H // 2
        self._canvas.create_text(px, py, text=char, fill=color, font=FONT)

    def render(self, stage: Stage, actors: List[Actor]) -> None:
        self._canvas.delete("all")

        for y in range(stage.height):
            for x in range(stage.width):
                tile = stage.get(x, y)
                fg, _ = COLOR_MAP.get(tile.color_pair, ("white", "black"))
                self._draw_char(x, y, tile.char, fg)

        for actor in actors:
            fg, _ = COLOR_MAP.get(actor.color_pair, ("white", "black"))
            self._draw_char(actor.x, actor.y, actor.char, fg)

            if actor.breed.name == "you":
                hud = f"Health: {actor.health}/{actor.breed.max_hp}"
                self._canvas.create_text(
                    4,
                    (stage.height + 1) * CELL_H,
                    text=hud,
                    fill="white",
                    font=FONT,
                    anchor="w",
                )
