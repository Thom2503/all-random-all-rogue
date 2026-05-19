from typing import List


class Energy:
    MIN_SPEED: int = 0
    NORMAL_SPEED: int = 3
    MAX_SPEED: int = 5
    ACTION_COST: int = 12

    GAINS: List[int] = [
        2,
        3,
        4,
        6,
        9,
        12
    ]

    energy: int = 0

    @staticmethod
    def tickSpeed(speed: int) -> float:
        return Energy.ACTION_COST / Energy.GAINS[Energy.NORMAL_SPEED + speed]

    def canTakeTurn(self) -> bool:
        return self.energy >= Energy.ACTION_COST

    def gain(self, speed: int) -> bool:
        self.energy += Energy.GAINS[speed]
        return self.canTakeTurn()

    def spend(self) -> None:
        assert self.energy >= Energy.ACTION_COST
        self.energy: int = self.energy % Energy.ACTION_COST
