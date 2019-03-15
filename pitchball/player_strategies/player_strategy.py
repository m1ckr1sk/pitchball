import math
import random


class PlayerStrategy:
    def attempt_return(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def return_success(self, to_player, from_player):
        if to_player.team == from_player.team:
            return random.randint(1, 2 + to_player.ability["defend"] + from_player.ability["passing"] // 2)
        else:
            return random.randint(1, 2 + max(to_player.ability["defend"] - from_player.ability["attack"] // 2, 0))
