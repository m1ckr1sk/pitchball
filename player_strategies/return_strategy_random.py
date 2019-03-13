import random

class RandomReturnStrategy:
    def __init__(self):
        self.return_attempt = {}

    def attempt_return(self, game_world, player):
        self.return_attempt["success_rating"] =  random.randint(1, 2 + player.ability["defense"])
        if player.team == "away":
            self.return_attempt["return_position"] = random.randint(7, 12)
        else:
            self.return_attempt["return_position"] = random.randint(1, 6)

        return self.return_attempt




