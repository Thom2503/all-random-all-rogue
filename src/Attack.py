from dataclasses import dataclass


@dataclass(frozen=True)
class Attack:
    minDmg: int
    maxDmg: int
    hitChn: int
    name: str
