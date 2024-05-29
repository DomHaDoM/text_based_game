from assets.constants import RARITY_CHANCES as rc
from assets.weapons import Weapon
from random import randint, choices

class Chest:
    def __init__(self, item_name: str) -> None:
        self.rarity = self.random_rarity()
        self.item = Weapon(name=item_name, damage=5, rarity=self.rarity)

    def random_rarity(self):
        numbers: list[int] = [i for i in range(1, 100)]
        for rarity, chance in rc.items():
            if randint(1, 100) in choices(population=numbers, k=chance):
                return rarity
        return "common"