from typing import Literal
from assets.characters import Boss, Enemy
from assets.chest import Chest



# variable for starting room
STARTING_ROOM: str = "room1"

# dictionary to put a map inside
MAP: dict[str, dict] = {
    "room1": {
        "forward": "room2"
        , "left": None
        , "right": None
        , "items": Chest().item
        , "enemies": []
        }
    , "room2": {
        "left": "room3"
        , "forward": "heal_room"
        , "enemies": [Enemy(20, 4)]
        , "items": Chest().item
        }
    , "room3": {

    }
    , "heal_room": {
        "right": "chest_room"
        , "left": "room4"
        , "forward": "upgrade_room"
        }
    , "room4": {

    }
    , "chest_room": {
        "chest": Chest().item
    }
    , "upgrade_room": {
        "right": "boss_room"
        }
    , "boss_room": {
        "enemies": Boss(100, 15)
    }
}