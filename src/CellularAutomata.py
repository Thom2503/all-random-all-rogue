from DefaultTiles import WALL, FLOOR
import random


class CellularAutomata:

    @staticmethod
    def fillStage(stage, w: int, h: int):
        def countNeighbours(x: int, y: int, r: int) -> int:
            x1: int = x - r
            x2: int = x + r
            y1: int = y - r
            y2: int = y + r
            count: int = 0

            for ny in range(y1, y2 + 1):
                for nx in range(x1, x2 + 1):
                    if stage.inBounds(nx, ny) and stage.get(nx, ny) is WALL:
                        count += 1
            return count

        def init(percentOfWall: int = 40) -> None:
            for y in range(h):
                for x in range(w):
                    if x == 0 or y == 0 or x == w - 1 or y == h - 1:
                        stage.set(x, y, WALL)
                    elif random.random() * 100 < percentOfWall:
                        stage.set(x, y, WALL)
                    else:
                        stage.set(x, y, FLOOR)

        def doFirstIteration(time: int) -> None:
            for i in range(time):
                for y in range(h):
                    for x in range(w):
                        if countNeighbours(x, y, 1) >= 9 - i or \
                           countNeighbours(x, y, 2) <= 9 - i:
                            stage.set(x, y, WALL)
                        else:
                            stage.set(x, y, FLOOR)

        def doSecondIteration(time: int) -> None:
            for _ in range(time):
                for y in range(h):
                    for x in range(w):
                        if countNeighbours(x, y, 1) >= 5 or \
                           x == 0 or \
                           y == 0 or \
                           x == w - 1 or \
                           y == h - 1:
                            stage.set(x, y, WALL)

        init(40)
        doFirstIteration(4)
        doSecondIteration(2)