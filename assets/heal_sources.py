from random import randint
from typing import NoReturn

class Flask:
    def _init_(self, charges: int) -> None:
        self.charges = charges

    def heal(self) -> int | NoReturn:
        healing_amount = randint(13, 19)
        if self.charges - 1 > 0:
            self.charges -= 1
            print(f"Healed for {healing_amount}. Charges left: {self.charges}")
            return healing_amount
        else:
            print("No Flask charges left")