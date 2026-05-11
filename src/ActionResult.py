from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Self
from Action import Action


@dataclass(frozen=True)
class ActionResult:
    succeeded: bool
    alternative: Action | None = None

    success: ClassVar[Self]
    failure: ClassVar[Self]

    @classmethod
    def alternate(cls, alternative: Action) -> Self:
        return cls(True, alternative)


ActionResult.success = ActionResult(True)
ActionResult.failure = ActionResult(False)
