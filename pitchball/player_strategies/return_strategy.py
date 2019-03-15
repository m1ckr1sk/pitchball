import random

class ReturnStrategy():

    def update_return_strategy(self, game_world, player):
        return

    def return_success(self, to_player, from_player):
        temporal_effect = 2
        success = temporal_effect
        if to_player.team == from_player.team:
            success += to_player.ability["defend"] + \
                from_player.ability["passing"] // 2
        else:
            success += max(to_player.ability["defend"] -
                           from_player.ability["attack"] // 2, 0)

        print(f'return : from {temporal_effect} to {success}')
        return random.randint(temporal_effect, success)
