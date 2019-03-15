import math
import random


class PlayerStrategy:
    def attempt_return(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def return_success(self, defender, attacker):
        return random.randint(1, 2 + max(defender.ability["defend"] - attacker.ability["attack"] // 2, 0))
