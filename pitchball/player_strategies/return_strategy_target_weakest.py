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
        
        attacker = game_world.get_player_at_position(game_world.get_previous_ball_position())
        home = list(range(7, 13))
        away = list(range(1, 7))
        if player.ability["defend"] > player.ability["passing"]:
            self.return_attempt["success_rating"] = super().return_success(player, attacker)
            weakest_player = self.find_weakest_opposition_player(game_world, player.team)
            if weakest_player is None:
                if player.team == "away":
                    self.return_attempt["return_position"] = random.choice(home)
                else:
                    self.return_attempt["return_position"] = random.choice(away)
            else:
                self.return_attempt["return_position"] = weakest_player.position
        else:
            self.return_attempt["success_rating"] =  random.randint(1, 2 + player.ability["passing"])
            strongest_attacker = self.find_strongest_attacker(game_world, player)
            if strongest_attacker is None:
                if player.team == "away":
                    away.remove(player.position)
                    self.return_attempt["return_position"] = random.choice(away)
                else:
                    home.remove(player.position)
                    self.return_attempt["return_position"] = random.choice(home)
            else:
                 self.return_attempt["return_position"] = strongest_attacker.position

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

    def find_strongest_attacker(self, game_world, current_player):

        my_team = game_world.teams[current_player.team]

        best_attack = 0
        best_attacker = None
        for player in my_team.players:
            if current_player.position != player.position:
                if player.ability["attack"] > best_attack:
                    best_attack = player.ability["attack"]
                    best_attacker = player
        
        print("Best is {}".format(best_attacker.surname))

        return best_attacker

        


