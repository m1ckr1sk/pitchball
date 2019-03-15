import random
from .pass_strategy import PassStrategy

class RandomPassStrategy(PassStrategy):

    def update_pass_strategy(self, game_world, player):
        
        return_attempt = {}
        from_player = game_world.get_player_at_position(game_world.get_previous_ball_position())
        home = list(range(7, 13))
        away = list(range(1, 7))
        return_attempt["success_rating"] =  super().pass_success(player, from_player)
        if player.team == "away":
            away.remove(player.position)
            return_attempt["return_position"] = random.choice(away)
        else:
            home.remove(player.position)
            return_attempt["return_position"] = random.choice(home)

        return return_attempt
