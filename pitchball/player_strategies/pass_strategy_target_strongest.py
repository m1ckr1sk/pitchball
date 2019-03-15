import random
from .pass_strategy import PassStrategy

class TargetStrongestPassStrategy(PassStrategy):

    def update_pass_strategy(self, game_world, player):
        return_attempt = {}
        from_player = game_world.get_player_at_position(game_world.get_previous_ball_position())
        home = list(range(7, 13))
        away = list(range(1, 7))
        return_attempt["success_rating"] =  super().pass_success(player, from_player)
        strongest_attacker = self.find_strongest_attacker(game_world, player)
        if strongest_attacker is None:
            if player.team == "away":
                away.remove(player.position)
                return_attempt["return_position"] = random.choice(away)
            else:
                home.remove(player.position)
                return_attempt["return_position"] = random.choice(home)
        else:
             return_attempt["return_position"] = strongest_attacker.position

        return return_attempt

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

        


