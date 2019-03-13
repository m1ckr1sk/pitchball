import random


class Player:
    def __init__(self, name, position, team, ability, return_strategy):
        self.position = position
        self.name = name
        self.team = team
        self.touches = 0
        self.misses = 0
        self.ability = ability
        self.return_strategy = return_strategy

    def set_return_strategy(self, return_strategy):
        self.return_strategy = return_strategy

    def update(self, game_world):
        if not game_world.the_ball.current_state_served:
            if game_world.get_current_ball_position() == self.position:
                if self.team == "away":
                    game_world.set_new_ball_position(random.randint(7, 12))
                else:
                    game_world.set_new_ball_position(random.randint(1, 6))
                game_world.set_served_state()
        else:
            # is the ball in my area
            if game_world.get_current_ball_position() == self.position:
                # Its with me so check if I can return it
                return_attempt = self.return_strategy.attempt_return(game_world, self)

                if return_attempt["success_rating"] > 2:
                    self.touches = self.touches + 1
                    game_world.set_new_ball_position(return_attempt["return_position"])
                else:
                    self.misses = self.misses + 1

                

    def surname(self):
        return self.name.split(" ")[1]
