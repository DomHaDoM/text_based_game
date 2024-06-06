from typing import Literal
from assets.weapons import Weapon
from assets.heal_sources import Flask
from assets.constants import MAP, STARTING_ROOM

class Character:
    max_health: int = 40
    def __init__(self, weapon: Weapon = Weapon()) -> None:
        self.current_health: int = self.max_health
        self.type = "character"
        self.weapon: Weapon = weapon
        self.damage = weapon.damage
        self.current_room: str = STARTING_ROOM
        self.previous_room: str = None
        self.flask_charges: int = 2


    def heal(self):
        """ function created to heal current character

        :param damage: int - number of damage to deal
        :return: None
        
        Updates current hp for the character
        """
        if self.flask_charges > 0:
            heal_amount = Flask(charges=self.flask_charges).heal()
            self.flask_charges = Flask.charges
            self.current_health = min(self.current_health + heal_amount, self.max_health) # check to avoid hp going over the max barrier
        else:
            Flask(charges=self.flask_charges).heal()

    def get_damage(self, damage: int) -> None:
        """ function created to get damage from characters

        :param damage: int - number of damage to deal
        :return: None
        
        Updates current hp for the character
        """
        self.current_health = max(self.current_health - damage, 0)  # check to avoid hp going lower than 0

    def deal_damage(self, opponent) -> None:
        """ function created to deal damage to other entities
        :param opponent - other entity
        :return: None - deals damage to other entity
        """
        opponent.get_damage(self.damage)

    def move(self, direction: Literal["forward", "left", "right"]) -> ValueError | None:
        """ Function created to move characters

        :param direction: Literal["forward", "left", "right"] - variation where to move next
        :return: None

        Move character to a new room
        """
        ## cheks proper value was passed in param: direction
        if direction not in ["forward", "left", "right"]:
            raise ValueError("incorrect direction")
        ## checks if player can go to this direction from current room
        if direction not in MAP[self.current_room]:
            raise ValueError("Can't go this direction from current room")
        self.previous_room = self.current_room
        self.current_room = MAP[self.current_room][direction]

    def move_to_previous_room(self) -> None:
        """ Function created for coming back to previous room
        
        Swaps values of previous and current rooms
        """
        self.current_room, self.previous_room = self.previous_room, self.current_room

class Hero(Character):
    def __init__(self, weapon: Weapon = Weapon()) -> None:
        super().__init__(weapon=weapon)
        self.type = "player"

    def __str__(self) -> str:
        return f"Class: {self.type}\n--Current Health: {self.current_health}\n--Damage: {self.damage}"



class Enemy(Character):
    def __init__(self, max_health: int, damage: int):
        super().__init__(damage=damage, max_health=max_health)
        self.current_health: int = max_health
        self.type = "enemy"
        self.enemy_class = "regular"


class Boss(Enemy):
    def __init__(self, max_health: int, damage: int):
        super().__init__(max_health=max_health, damage=damage)
        self.enemy_class = "boss"

    def special_ability(self) -> NotImplementedError:
        raise NotImplementedError("Create an ability for boss to swap theme mode of the page")