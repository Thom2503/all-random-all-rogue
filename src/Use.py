from abc import ABC, abstractmethod


class Use(ABC):
    @abstractmethod
    def use() -> None:
        pass
