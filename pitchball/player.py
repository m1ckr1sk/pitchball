import random
from .player_strategies.player_strategy import PlayerStrategy


class Player:
    def __init__(self, name, position, team, ability, return_strategy):
        self._position = position
        self._name = name
        self._team = team
        self._touches = 0
        self._misses = 0
        self._ability = ability
        self._return_strategy = return_strategy

    @property
    def position(self):
        return self._position

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self.name.split(" ")[1]

    @property
    def team(self):
        return self._team

    @property
    def touches(self):
        return self._touches

    @property
    def misses(self):
        return self._misses

    @property
    def ability(self):
        return self._ability

    @property
    def return_strategy(self):
        return self._return_strategy

    @return_strategy.setter
    def return_strategy(self, return_strategy):
        if issubclass(return_strategy, PlayerStrategy):
            raise TypeError("player strategy must inherit from PlayerStrategy")
        self._return_strategy = return_strategy

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
                return_attempt = self.return_strategy.attempt_return(
                    game_world, self)

                if return_attempt["success_rating"] > 2:
                    self._touches = self._touches + 1
                    game_world.set_new_ball_position(
                        return_attempt["return_position"])
                else:
                    self._misses = self._misses + 1

