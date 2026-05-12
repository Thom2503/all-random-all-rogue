from Action import Action
from ActionResult import ActionResult


class WaitAction(Action):
    """
    Sometimes NPCs or others must wait or are stunned, so this is kind of a
    hack to make them stop for a while.

    Methods:
    perform(self) -> ActionResult - returns the success
    """

    def perform(self) -> ActionResult:
        """
        Not really interesting but it just makes the game loop "wait" because
        it only returns success

        Parameters:
        self (Self) - the action

        Returns:
        ActionResult.success (ActionResult) - success
        """
        return ActionResult.success