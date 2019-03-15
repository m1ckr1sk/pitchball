import random
from .return_strategy import ReturnStrategy


class TargetWeakestReturnStrategy(ReturnStrategy):

    def update_return_strategy(self, game_world, player):

        return_attempt = {}
        from_player = game_world.get_player_at_position(
            game_world.get_previous_ball_position())
        home = list(range(7, 13))
        away = list(range(1, 7))
        return_attempt["success_rating"] = super(
        ).return_success(player, from_player)
        weakest_player = self.find_weakest_opposition_player(
            game_world, player.team)
        if weakest_player is None:
            if player.team == "away":
                return_attempt["return_position"] = random.choice(home)
            else:
                return_attempt["return_position"] = random.choice(away)
        else:
            return_attempt["return_position"] = weakest_player.position

        return return_attempt

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
