from DefaultTiles import WALL, FLOOR
import random


class CellularAutomata:
    """
    CellularAutomata class to generate terrain using cellular automat, now very
    basic but want to make more dynamic.
    """

    @staticmethod
    def fillStage(
        stage,
        w: int,
        h: int,
        percentOfWall: int = 40,
        time: int = 4
    ) -> None:
        """
        fill the stage using the cellular automata way by checking the
        neighbours and doing multiple passes. Do two iterations for now.

        NOTE: Time is halved each iteration

        Parameters:
        stage (Stage) - the stage to fill the terrain in
        w (int) - the width of the room
        h (int) - the height of the room
        percentOfWall (int) = 40 - percentage of wall in init()
        time (int) = 4 - the amount of passes in each iteration
        """
        def countNeighbours(x: int, y: int, r: int) -> int:
            """
            Count the neighbours around the current cell, used to determine
            where walls and floors need to be placed.

            Parameters:
            x (int) - the x coord
            y (int) - the y coord
            r (int) - the range of the neighbours

            Returns:
            count (int) - the amount of neighbours
            """
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
            """
            do a first pass to fill the walls randomly, depends on the seed,
            and the percentage is from the parameter.

            Parameters:
            percentOfWall (int) = 40 - the percentage that needs to be wall
            """
            for y in range(h):
                for x in range(w):
                    if x == 0 or y == 0 or x == w - 1 or y == h - 1:
                        stage.set(x, y, WALL)
                    elif random.random() * 100 < percentOfWall:
                        stage.set(x, y, WALL)
                    else:
                        stage.set(x, y, FLOOR)

        def doFirstIteration(time: int) -> None:
            """
            do the first iteration over the room to determine the floors and
            walls based on the neighbours, where the time has impact

            Parameters:
            time (int) - the amount of passes needed to be done
            """
            for i in range(time):
                for y in range(h):
                    for x in range(w):
                        if countNeighbours(x, y, 1) >= 9 - i or \
                           countNeighbours(x, y, 2) <= 9 - i:
                            stage.set(x, y, WALL)
                        else:
                            stage.set(x, y, FLOOR)

        def doSecondIteration(time: int) -> None:
            """
            do the second iteration over the room to determine the floors and
            walls based on the neighbours, time has no impact

            Parameters:
            time (int) - the amount of passes needed to be done
            """
            for _ in range(time):
                for y in range(h):
                    for x in range(w):
                        if countNeighbours(x, y, 1) >= 5 or \
                           x == 0 or \
                           y == 0 or \
                           x == w - 1 or \
                           y == h - 1:
                            stage.set(x, y, WALL)

        init(percentOfWall)
        doFirstIteration(time)
        doSecondIteration(time//2)