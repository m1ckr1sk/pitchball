import random
from .player_strategy import PlayerStrategy

class PlayerStrategyRandom(PlayerStrategy):

    def __init__(self, players_pass_strategy, players_return_strategy):
        super().__init__(players_pass_strategy, players_return_strategy)
    
    def update_player_strategy(self, game_world, player):
        pass_or_return = random.choice([0,1])
        if pass_or_return == 0:
            return self.players_pass_strategy.update_pass_strategy(game_world, player)
        else:
            return self.players_return_strategy.update_return_strategy(game_world, player)