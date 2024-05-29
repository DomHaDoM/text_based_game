# Own assets
from assets.characters import Hero, Enemy, Boss
from assets.weapons import Weapon
# Typing
from typing import Literal
# # Random
# from random import randint

version = "0.1"

class Game:
    # Initializaiton of the class
    def __init__(self, difficulty: Literal["easy", "medium", "hard", "insane"]) -> None:
        # difficulty level and multipiers
        self.difficulty: str = difficulty.lower()
        self.enemy_hp_multiplier, self.enemy_dmg_multiplier = self.enemy_difficulty(difficulty)
        self.boss_muliplier: int = 3.

        # Players and enemies
        self.player: Hero = self.create_player()
        self.enemies: dict[str, list] = {"enemies": [], "bosses": []}

    # Function used to create playble character (Hero)
    def create_player(self, weapon: Weapon | None = None) -> Hero:
        return Hero() if weapon is None else Hero(weapon=weapon)
    
    def create_enemy(self, hp: int, type: Literal["regular", "boss"], dmg: int) -> Enemy | ValueError:
        if type == "regular":
            self.enemies["enemies"].append(
                Enemy(max_health=hp * self.enemy_hp_multiplier
                      , damage=dmg * self.enemy_dmg_multiplier)
                      )
        elif type == "boss":
            self.enemies["bosses"].append(
                Boss(max_health=hp * self.enemy_hp_multiplier * self.boss_muliplier
                     , damage=dmg * self.enemy_dmg_multiplier * self.boss_muliplier
                     )
                )
        else:
            raise ValueError(f"Incorrect enemy type: {"*Boss* or *regular enemy*"}")

    @staticmethod
    # Function that determines game difficulty multiplier
    def enemy_difficulty(difficulty: str) -> tuple[float, float]:
        if difficulty == "easy":
            return .75, .5
        elif difficulty == "medium":
            return 1., 1.
        elif difficulty == "hard":
            return 1.5, 1.25
        elif difficulty == "insane":
            return 3., 2.5

    @property
    # Player Information
    def player_info(self) -> str:
        return self.player.__str__()
    
    @property    
    # Returns current settings
    def current_settings(self) -> None:
        return f"Current Player\n---{self.player_info}\nCurrent difficulty: {self.difficulty.title()}\nMultipiers:\n---Enemy HP: {self.enemy_hp_multiplier*100:2}%\n---Enemy Damage: {self.enemy_dmg_multiplier*100:2}%"