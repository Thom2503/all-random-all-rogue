from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar, Self, TYPE_CHECKING

if TYPE_CHECKING:
    from Action import Action


@dataclass(frozen=True)
class ActionResult:
    """
    ActionResult object to determine if an action is handled successfully
    and if so what to do next. Use alternative to define different actions
    to perform when it failed.

    Methods:
    alternate(cls, alternative) -> Self - the alternative action constructor
    """

    succeeded: bool
    alternative: Action | None = None
    success: ClassVar[Self]
    failure: ClassVar[Self]

    @classmethod
    def alternate(cls, alternative: Action) -> Self:
        """
        Constructor method for the alternative action if it didn't succeed

        Parameters:
        cls (Self) - this class instance
        alternative (Action) - the alternative action to do

        Returns:
        Self - the new object with the correct constructor
        """
        return cls(True, alternative)


ActionResult.success = ActionResult(True)
ActionResult.failure = ActionResult(False)
