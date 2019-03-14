import random
from .world import World


class Commentary:
    def __init__(self):
        self.return_text = [
            'smashed it back at',
            'dived for and just managed to get it over the net towards',
            'overhanded the ball over the net straight at']
        self.pass_text = ['given the ball to', 'passed it to',
                          'sharply given it to', 'put it in the path of']

    def intro(self, game_world):
        print('your match is against {}'.format(game_world.teams["away"].name))
        print(
            "\n".join(team.name for team in game_world.teams["home"].players))
        print('  This is your final team.  May you achieve victory and glory with them!')

    def update(self, game_world):
        if not game_world.the_ball.current_state_served:
            self.print_service(game_world)
        else:
            if game_world.get_current_ball_position() == game_world.get_new_ball_position():
                # the ball hasn't moved so someone has scored
                self.print_scoring_shot(game_world)
            else:
                # ball has moved but is it a pass or return
                self.print_non_scoring_shot(game_world)

        # self.print_tactics(game_world)

        self.print_pitch(game_world)

    def print_tactics(self, game_world):
        player_in_position = game_world.get_player_at_position(
            game_world.get_current_ball_position())

        print("{} strategy is {}".format(
            player_in_position.surname,
            player_in_position.return_strategy))

    def print_non_scoring_shot(self, game_world):
        player_in_position = game_world.get_player_at_position(
            game_world.get_current_ball_position())
        player_in_target_position = game_world.get_player_at_position(
            game_world.get_new_ball_position())

        if player_in_position.team == \
                player_in_target_position.team:
            # pass
            print("{} has {} {}".format(player_in_position.name,
                                        random.choice(self.pass_text),
                                        player_in_target_position.name))
        else:
            # return
            print("{} has {} {}!".format(player_in_position.name,
                                         random.choice(self.return_text),
                                         player_in_target_position.name))

    def print_scoring_shot(self, game_world):
        player_in_position = game_world.get_player_at_position(
            game_world.the_ball.current_position)
        print("{} has missed the return!".format(
            player_in_position.name))
        print("Score is {} {}".format(
            game_world.home_score, game_world.away_score))

    def print_service(self, game_world):
        serving_player = game_world.get_player_at_position(
            game_world.get_current_ball_position())
        player_in_target_position = game_world.get_player_at_position(
            game_world.get_new_ball_position())
        print("{} takes the ball and serves towards {}".format(
            serving_player.surname, player_in_target_position.surname))

    def print_pitch(self, game_world):
        position = 12
        for x in range(0, 4):
            if x == 2:
                print("".center(60, '-'))
                print("".center(60, 'x'))
                print("".center(60, '-'))
            else:
                print("".center(60, '-'))
            for pos_index in range(0, 3):
                if position - pos_index != game_world.the_ball.current_position:
                    print("{}".format(game_world.get_player_at_position(
                        position - pos_index).surname).center(20), end='')
                else:
                    print("({})".format(game_world.get_player_at_position(
                        position - pos_index).surname).center(20), end='')
            print()
            for pos_index in range(0, 3):
                print("{} {}".format(
                    game_world.get_player_at_position(
                        position - pos_index).touches,
                    game_world.get_player_at_position(
                        position - pos_index).misses
                ).center(20), end='')
            print()
            position = position - 3

        print("".center(60, '-'))

    def final_result(self, game_world):
        if game_world.home_score > game_world.away_score:
            print("{} {} {} win!".format(game_world.home_score,
                                         game_world.away_score,
                                         game_world.teams["home"].name))
        elif game_world.home_score < game_world.away_score:
            print("{} {} {} win!".format(game_world.home_score,
                                         game_world.away_score,
                                         game_world.teams["away"].name))
        else:
            print("{} {} It's a tie".format(
                game_world.home_score, game_world.away_score))

    def statistics(self, game_world):
        print("{} team stats:".format(game_world.teams["home"].name))
        self.print_team_stats(game_world.teams["home"].players)

        print("{} team stats:".format(game_world.teams["away"].name))
        self.print_team_stats(game_world.teams["away"].players)

    def print_team_stats(self, players):
        self.print_stats_header()
        for player in players:
            print("{}({})".format(player.name,
                                  player.ability["defense"]).ljust(30), end='')
            print("| {}".format(player.touches).ljust(20), end='')
            print("| {}".format(player.misses).ljust(20), end='')
            print("|")

    def print_stats_header(self):
        print("Name".ljust(30), end='')
        print("| Touches".ljust(20), end='')
        print("| Mistakes".ljust(20) + "|")
