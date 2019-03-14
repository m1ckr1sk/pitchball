import random
from .player_strategy import PlayerStrategy

class RandomReturnStrategy(PlayerStrategy):
    def __init__(self):
        self.return_attempt = {}

    def __repr__(self):
        return "<RandomReturnStrategy return_attempt={}>".format(self.return_attempt)

    def __str__(self):
        return "RandomReturnStrategy {}".format(self.return_attempt)

    def attempt_return(self, game_world, player):
        
        pass_or_return = random.randint(0,1)
        home = list(range(7, 13))
        away = list(range(1, 7))
        if pass_or_return == 0:
            self.return_attempt["success_rating"] =  random.randint(1, 2 + player.ability["defense"])
            if player.team == "away":
                self.return_attempt["return_position"] = random.choice(home)
            else:
                self.return_attempt["return_position"] = random.choice(away)
        else:
            self.return_attempt["success_rating"] =  random.randint(1, 2 + player.ability["passing"])
            if player.team == "away":
                away.remove(player.position)
                self.return_attempt["return_position"] = random.choice(away)
            else:
                home.remove(player.position)
                self.return_attempt["return_position"] = random.choice(home)

        return self.return_attempt
