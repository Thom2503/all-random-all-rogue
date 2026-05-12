from abc import ABC, abstractmethod
from typing import Self
from ActionResult import ActionResult


class Action(ABC):
    """
    Abstract class for the action objects, inherit this to perform an action
    with perform()

    Methods:
    perform(self) -> ActionResult - perform an action, inherit this
    """

    @abstractmethod
    def perform(self: Self) -> ActionResult:
        """
        perform an action return a result from that action

        Parameters:
        self (Self) - this object

        Returns:
        ActionResult - the result of the performed action
        """
        pass
