from typing import Literal

POSSIBLE_WEAPONS: dict[str, int] = {
    "fists": 2
    , "sword": 5
    , "rapier": 12
    , "hammer": 8
    , "knife": 6
}

# dictionary with drarity drop chances
RARITY_CHANCES: dict[str, int | float] = {
    "rare": 25
    , "epic": 12
    , "mythic": 3
}

class Weapon:
    _multipliers: dict[str, float] = {"common": 1.
                                      , "rare": 1.25
                                      , "epic": 1.75
                                      , "mythic": 3
                                      } 
    _possible_weapons = POSSIBLE_WEAPONS.copy()
    def __init__(self, name: str = "fists", rarity: Literal["common", "rare", "epic", "mythic"] = "common") -> None:
        if name not in self._possible_weapons.keys():
            raise ValueError(f"'{name}' weapon type doesn't exist")
        self.name = name
        if rarity not in ["common", "rare", "epic", "mythic"]:
            raise ValueError(f"'{rarity}' rarity doesn't exist")
        self.rarity = rarity
        self.damage = self._possible_weapons[self.name] * Weapon._multipliers[rarity]

    def __str__(self) -> str:
        return f"Weapon: {self.name}\n--Rarity: {self.rarity}\n--Damage: {self.damage}"