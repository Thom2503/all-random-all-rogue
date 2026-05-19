from Action import Action
from Actor import Actor
from typing import Self
from ActionResult import ActionResult
from Game import Game
import random


class AttackAction(Action):
    _attacker: Actor
    _defender: Actor
    _game: Game

    def __init__(self, attacker: Actor, defender: Actor, game: Game) -> None:
        super().__init__()
        self._attacker = attacker
        self._defender = defender
        self._game = game

    def perform(self: Self) -> ActionResult:
        roll = random.randint(0, 100)
        eff_chance = self._attacker.hit_chance - self._defender.defence
        if roll > eff_chance:
            return ActionResult.success  # miss, turn is used

        attack = self._attacker.breed.attack
        dmg = random.randint(attack.minDmg, attack.maxDmg)
        died = self._defender.takeDamage(dmg)
        if died:
            self._game.removeActor(self._defender)

        return ActionResult.success
