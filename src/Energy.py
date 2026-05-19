from typing import List, Self


class Energy:
    """
    Energy class keep track of each energy of each actor, if you can walk or
    take an action depends on this class.

    Methods:
    tickSpeed(speed: int) -> float - determine the tickspeed is mostly for
                                     printing
    canTakeTurn(self) -> bool - if a turn can be taken by an actor
    gain(self, speed: int) -> bool - gain some energy and see if you can take a
                                     turn
    spend(self) -> None - spend some energy
    """
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
        """
        determine the current tick speed based on the energies and the actions
        by each actor, mostly for printing and stuff

        Parameters:
        speed (int) - the current speed

        Returns:
        float - the tick speed
        """
        return Energy.ACTION_COST / Energy.GAINS[Energy.NORMAL_SPEED + speed]

    def canTakeTurn(self: Self) -> bool:
        """
        if an actor can take a turn based on the current energy and the cost of
        an action

        Parameters:
        self (Self) - this object

        Returns:
        bool - if you can take a turn
        """
        return self.energy >= Energy.ACTION_COST

    def gain(self: Self, speed: int) -> bool:
        """
        gain some energy when an action is done

        Parameters:
        self (Self) - this object
        speed (int) - what the action takes

        Returns
        bool - if you can now take a turn
        """
        self.energy += Energy.GAINS[speed]
        return self.canTakeTurn()

    def spend(self: Self) -> None:
        """
        spend some energy on an action

        Throws an assert if the energy is higher than the action cost

        Parameters:
        self (Self) - this object
        """
        assert self.energy >= Energy.ACTION_COST
        self.energy: int = self.energy % Energy.ACTION_COST
