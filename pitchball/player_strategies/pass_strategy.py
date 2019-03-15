import random

class PassStrategy():

    def update_pass_strategy(self, game_world, player):
        return

    def pass_success(self, to_player, from_player):
        success = 2
        if to_player.team == from_player.team:
            success += to_player.ability["passing"] + \
                from_player.ability["passing"] // 2
        else:
            success += max(to_player.ability["defend"] - \
                from_player.ability["attack"] // 2, 0)
            
        return random.randint(1, success)