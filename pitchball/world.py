import random
import names
from .ball import Ball
from .team import Team
from .player import Player
from .player_strategies import RandomReturnStrategy
from .player_strategies import RandomPassStrategy
from .player_strategies import TargetStrongestPassStrategy
from .player_strategies import TargetWeakestReturnStrategy
from .player_strategies import PlayerStrategyRandom


class World:
    def __init__(self):
        self.teams = {}

        self.teams["home"] = Team()
        self.teams["away"] = Team()

        self.the_ball = Ball()

        self.home_score = 0
        self.away_score = 0

        return_random = RandomReturnStrategy()
        pass_random = RandomPassStrategy()
        pass_targeted = TargetStrongestPassStrategy()
        return_targeted = TargetWeakestReturnStrategy()
        

        self.random_strategy = PlayerStrategyRandom(
                                pass_random, 
                                return_random)

        self.target_strategy = PlayerStrategyRandom(
                                pass_targeted, 
                                return_targeted)

    def update(self):
        for player in self.teams["home"].players:
            player.update(self)
        for player in self.teams["away"].players:
            player.update(self)

        if self.the_ball.current_state_served:
            if self.the_ball.current_position == self.the_ball.new_position:
                # the ball hasn't moved so someone has scored
                if self.the_ball.current_position < 7:
                    self.home_score = self.home_score + 1
                else:
                    self.away_score = self.away_score + 1

                self.the_ball.new_state_served = False

    def swap_buffers(self):
        self.the_ball.swap_buffers()

    def generate_teams(self, home_team_name, away_team_name):
        self.generate_home_team()

        self.generate_away_team()

        self.teams["home"].name = home_team_name
        self.teams["away"].name = away_team_name

    def generate_team_abilities(self, totals, number_of_players):
        team_abilities = {}
        team_abilities["defend"] = self.generate_team_ability(number_of_players, totals[0])
        team_abilities["attack"] = self.generate_team_ability(number_of_players, totals[1])
        team_abilities["passing"] = self.generate_team_ability(number_of_players, totals[2])
        team_abilities["form"] = self.generate_team_ability(number_of_players, totals[2])
        team_abilities["fitness"] = self.generate_team_ability(number_of_players, totals[2])
        self.print_team_ability(team_abilities, "defend")
            

        return team_abilities

    def print_team_ability(self, team_abilities, ability_name):
        for ability in team_abilities[ability_name] :
            print("{} {}".format(ability_name, ability))

    def generate_team_ability(self, number_of_players, total):
        abilities = []

        # give at least one point to the ability
        for player_index in range(0,number_of_players):
            abilities.append(1)

        # randomly distribute the remaining points across the players
        running_total = total - number_of_players
        while running_total > 0:
            player_index = random.randint(0,number_of_players-1)
            if abilities[player_index] < 10:
                abilities[player_index] = abilities[player_index] + 1
            running_total = running_total - 1

        return abilities

    def get_player_ability(self, player_index, team_abilities):
        player_ability = {}
        player_ability["defend"] = team_abilities["defend"][player_index]
        player_ability["attack"] = team_abilities["attack"][player_index]
        player_ability["passing"] = team_abilities["passing"][player_index]
        player_ability["form"] = team_abilities["form"][player_index]
        player_ability["fitness"] = team_abilities["fitness"][player_index]
        return player_ability


    def generate_home_team(self):
        team_ability = self.generate_team_abilities((25, 25, 25, 25, 25), 6)
        
        for my_player_index in range(7, 13):
            self.teams["home"].players.append(
                self.generate_player(
                    my_player_index, 
                    "home", 
                    self.get_player_ability(my_player_index - 7, team_ability),
                    self.target_strategy))

    def generate_player(self, my_player_index, team, ability, strategy):
        return Player(
            names.get_full_name(),
            my_player_index,
            team,
            ability,
            strategy)

    def generate_away_team(self):
        team_ability = self.generate_team_abilities((25, 25, 25, 25, 25), 6)
        for opp_player_index in range(1, 7):
            self.teams["away"].players.append(
                self.generate_player(
                    opp_player_index, 
                    "away", 
                    self.get_player_ability(opp_player_index - 1, team_ability),
                    self.random_strategy))

    def choose_team_to_serve(self):
        if random.randint(0, 1) == 0:
            self.set_current_ball_position(random.choice(
                self.teams["home"].players).position)
        else:
            self.set_current_ball_position(random.choice(
                self.teams["away"].players).position)

    def get_previous_ball_position(self):
        return self.the_ball.previous_position

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
