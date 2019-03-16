import random


class PassStrategy():

    def update_pass_strategy(self, game_world, player):
        return

    def pass_success(self, to_player, from_player):

        min_base_chance = 1
        max_base_chance = 1
        if to_player.team == from_player.team:
            # ball from team to return
            to_boosted = to_player.ability["passing"] + \
                to_player.ability["form"] + \
                to_player.ability["fitness"]
            from_boosted = from_player.ability["passing"] + \
                from_player.ability["form"] + \
                from_player.ability["fitness"]

            max_base_chance = to_player.ability["passing"] + \
                to_boosted + \
                from_boosted // 2
        else:
            to_boosted = to_player.ability["passing"] + \
                to_player.ability["form"] + \
                to_player.ability["fitness"]
            from_boosted = from_player.ability["attack"] + \
                from_player.ability["form"] + \
                from_player.ability["fitness"]

            max_base_chance = to_player.ability["passing"] + \
                max((to_boosted -
                     from_boosted // 2), 0)

        print(f'pass : from {min_base_chance} to {max_base_chance}')
        return random.randint(min_base_chance, max_base_chance)
