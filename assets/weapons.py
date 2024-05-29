from typing import Literal

class Weapon:
    _multipliers: dict[str, float] = {"common": 1.
                                      , "rare": 1.25
                                      , "epic": 1.75
                                      , "mythic": 3
                                      } 
    def __init__(self, name: str, damage: int, rarity: Literal["common", "rare", "epic", "mythic"] = "common") -> None:
        self.name = name
        self.rarity = rarity
        self.damage = damage * Weapon._multipliers[rarity]

    def __str__(self) -> str:
        return f"Weapon: {self.name}\n--Rarity: {self.rarity}\n--Damage: {self.damage}"

fists = Weapon(name="fists", damage=2)
sword = Weapon(name="sword", damage=5)