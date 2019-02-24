import random
import names
from ball import Ball
from team import Team
from player import Player


class World:
    def __init__(self):
        self.teams = {}

        self.teams["home"] = Team()
        self.teams["away"] = Team()

        self.the_ball = Ball()

        self.home_score = 0
        self.away_score = 0

    def update(self):
        for player in self.teams["home"].players:
            player.update(self)
        for player in self.teams["away"].players:
            player.update(self)

        if self.the_ball.current_state_served:
            if self.the_ball.current_position == self.the_ball.new_position:
                # the ball hasn't moved so someone has scored
                if self.the_ball.current_position < 7:
                    self.away_score = self.away_score + 1
                else:
                    self.home_score = self.home_score + 1

                self.the_ball.new_state_served = False

    def swap_buffers(self):
        self.the_ball.swap_buffers()

    def generate_teams(self, home_team_name, away_team_name):
        for my_player_index in range(7, 13):
            self.teams["home"].players.append(
                Player(names.get_full_name(), my_player_index, "home", {"defense" : random.randint(1,10)}))

        for opp_player_index in range(1, 7):
            self.teams["away"].players.append(
                Player(names.get_full_name(), opp_player_index, "away", {"defense" : random.randint(1,10)}))

        self.teams["home"].name = home_team_name
        self.teams["away"].name = away_team_name

    def choose_team_to_serve(self):
        if random.randint(0, 1) == 0:
            self.set_current_ball_position(random.choice(
                self.teams["home"].players).position)
        else:
            self.set_current_ball_position(random.choice(
                self.teams["away"].players).position)

    def get_current_ball_position(self):
        return self.the_ball.current_position

    def get_new_ball_position(self):
        return self.the_ball.new_position

    def set_current_ball_position(self, position):
        self.the_ball.current_position = position

    def set_new_ball_position(self, position):
        self.the_ball.new_position = position

    def set_served_state(self):
        self.the_ball.new_state_served = True

    def get_player_at_position(self, position):
        player_to_return = None
        if position < 7:
            for player in self.teams["away"].players:
                if player.position == position:
                    player_to_return = player
                    break
        else:
            for player in self.teams["home"].players:
                if player.position == position:
                    player_to_return = player
                    break
        return player_to_return
