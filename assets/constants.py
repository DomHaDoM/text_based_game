# dictionary to put a map inside
MAP: dict[str, dict[str, str]] = {}

# variable for starting room
STARTING_ROOM: str = None

# dictionary with drarity drop chances
RARITY_CHANCES: dict[str, int | float] = {
    "rare": 25
    , "epic": 12
    , "mythic": 3
}