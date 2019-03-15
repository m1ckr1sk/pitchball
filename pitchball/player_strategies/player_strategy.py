from .pass_strategy import PassStrategy
from .return_strategy import ReturnStrategy

class PlayerStrategy():

    def __init__(self, 
                players_pass_strategy, 
                players_return_strategy):
        self.players_pass_strategy = players_pass_strategy
        self.players_return_strategy = players_return_strategy
    
    def update_player_strategy(self, game_world, player):
        pass
        