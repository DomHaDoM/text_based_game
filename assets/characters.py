from assets.weapons import Weapon, fists

class Character:
    max_health: int = 40
    default_damage: int = 5
    def __init__(self, weapon: Weapon) -> None:
        self.current_health: int = self.max_health
        self.type = "character"
        self.weapon: Weapon = weapon
        self.damage = weapon.damage

    def heal(self, heal_amount: int):
        self.current_health = min(self.current_health+heal_amount, self.max_health)

    def get_damage(self, damage: int) -> None:
        self.current_health = max(self.current_health - damage, 0)

    def deal_damage(self, opponent) -> None:
        opponent.get_damage(self.damage)


class Hero(Character):
    def __init__(self, weapon: Weapon = fists) -> None:
        super().__init__(weapon=weapon)
        self.type = "player"
        # self.damage = Character.default_damage

    def __str__(self) -> str:
        return f"Class: {self.type}\n--Current Health: {self.current_health}\n--Damage: {self.damage}"



class Enemy(Character):
    def __init__(self, max_health: int, damage: int, weapon: Weapon):
        super().__init__(weapon=weapon)
        self.current_health: int = max_health
        self.type = "enemy"
        self.enemy_class = "regular"


class Boss(Enemy):
    def __init__(self, max_health: int, damage: int):
        super().__init__(max_health=max_health, damage=damage)
        self.enemy_class = "boss"

    def special_ability(self) -> NotImplementedError:
        raise NotImplementedError("Create an ability for boss to swap theme mode of the page")