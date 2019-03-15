import random
from .player_strategies.player_strategy import PlayerStrategy
from .property_closures import typedproperty, roproperty

class Player:
    
    position = roproperty("position")
    name = roproperty("name")
    team = roproperty("team")
    touches = roproperty("touches")
    misses = roproperty("misses")
    ability = roproperty("ability")
    strategy = typedproperty("strategy", PlayerStrategy)
    

    def __init__(self, name, position, team, ability, strategy):
        self._position = position
        self._name = name
        self._team = team
        self._touches = 0
        self._misses = 0
        self._ability = ability
        self._strategy = strategy

    @property
    def surname(self):
        return self.name.split(" ")[1]

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
                return_attempt = self._strategy.update_player_strategy(
                    game_world, self)

                if return_attempt["success_rating"] > 2:
                    self._touches = self._touches + 1
                    game_world.set_new_ball_position(
                        return_attempt["return_position"])
                else:
                    self._misses = self._misses + 1

