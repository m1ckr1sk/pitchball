import random
from .player_strategy import PlayerStrategy

class TargetWeakestReturnStrategy(PlayerStrategy):
    def __init__(self):
        self.return_attempt = {}

    def __repr__(self):
        return "<TargetWeakestReturnStrategy return_attempt={}>".format(self.return_attempt)

    def __str__(self):
        return "TargetWeakestReturnStrategy {}".format(self.return_attempt)

    def attempt_return(self, game_world, player):
        
        self.return_attempt["success_rating"] = random.randint(1, 2 + player.ability["defense"])
        weakest_player = self.find_weakest_opposition_player(game_world, player.team)
        if weakest_player is None:
            if player.team == "away":
                self.return_attempt["return_position"] = random.randint(7, 12)
            else:
                self.return_attempt["return_position"] = random.randint(1, 6)
        else:
            self.return_attempt["return_position"] = weakest_player.position
        return self.return_attempt
    
    def find_weakest_opposition_player(self, game_world, team):
        oppo_team = "home"
        if team == "home":
            oppo_team = "away"

        oppo_team = game_world.teams[oppo_team]

        most_mistakes = 0
        weakest_player = None
        for player in oppo_team.players:
            if player.misses > most_mistakes:
                most_mistakes = player.misses
                weakest_player = player

        return weakest_player

        


