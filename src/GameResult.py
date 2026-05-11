from typing import Optional
from Action import Action
from typing_extensions import Self


class GameResult:
    alternative: Optional[Action]
    succeeded: Optional[bool]
    failure: Self
    success: Self

    def __init__(
        self: Self,
        succeed: Optional[bool] = None,
        alternative: Optional[Action] = None
    ) -> None:
        self.succeeded = succeed
        self.alternative = alternative

    @classmethod
    def frombool(cls, succeed: bool) -> Self:
        cls.succeeded = succeed
        cls.alternative = None
        return cls(succeed=succeed)

    @classmethod
    def fromaction(cls, alternative: Action) -> Self:
        cls.alternative = alternative
        cls.succeeded = True
        return cls(alternative=alternative)
