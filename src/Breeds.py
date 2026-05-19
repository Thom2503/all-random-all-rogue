from Breed import Breed
from Attack import Attack
from Energy import Energy

PLAYER = Breed(
    name="you",
    app="@",
    speed=Energy.NORMAL_SPEED,
    max_hp=20,
    attack=Attack(1, 3, 80, "punch"),
    defence=10,
    hit_chance=80,
    canOpenDoors=True,
    moves=[],
    flags=set(),
)

PIENUS = Breed(
    name="pienus",
    app="P",
    speed=Energy.NORMAL_SPEED,
    max_hp=20,
    attack=Attack(1, 2, 60, "scratch"),
    defence=10,
    hit_chance=80,
    canOpenDoors=True,
    moves=[],
    flags=set(),
)
