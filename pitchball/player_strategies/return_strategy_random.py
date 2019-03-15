import random
from .return_strategy import ReturnStrategy

class RandomReturnStrategy(ReturnStrategy):
    def update_return_strategy(self, game_world, player):

        return_attempt = {}
        from_player = game_world.get_player_at_position(game_world.get_previous_ball_position())
        
        home = list(range(7, 13))
        away = list(range(1, 7))

        return_attempt["success_rating"] = super().return_success(player, from_player)
        if player.team == "away":
            return_attempt["return_position"] = random.choice(home)
        else:
            return_attempt["return_position"] = random.choice(away)

        return return_attempt
