from assets.constants import RARITY_CHANCES, POSSIBLE_WEAPONS
from assets.weapons import Weapon
from random import choice, randint, choices

class Chest:
    def __init__(self) -> None:
        self.rarity = self.random_rarity()
        weapon_name = choice(POSSIBLE_WEAPONS.keys())
        self.item = Weapon(name=weapon_name, rarity=self.random_rarity())

    def random_rarity(self):
        numbers: list[int] = [i for i in range(1, 100)]
        for rarity, chance in RARITY_CHANCES.items():
            if randint(1, 100) in choices(population=numbers, k=chance):
                return rarity
        return "common"