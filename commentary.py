from world import World
import random


class Commentary:
    def __init__(self):
        self.return_text = [
            'smashed it back', 'dived for and just managed to get it over the next', 'overhands the ball over the net']
        self.pass_text = [' gives the ball to ', ' passes it to ',
                          ' sharply gives it to ', ' puts it in the path of ']
        self.defend_text = [' performs a great tackle ',
                            ' comes up with a meaty tackle ']

    def intro(self, game_world):
        print('your match is against {}'.format(game_world.teams["away"].name))
        print(
            "\n".join(team.name for team in game_world.teams["home"].players))
        print('  This is your final team.  May you achieve victory and glory with them!')

    def update(self, game_world):
        if not game_world.the_ball.current_state_served:
            serving_player = game_world.get_player_at_position(
                game_world.get_current_ball_position())
            print("{} takes the ball and serves".format(
                serving_player.surname()))
        else:
            if game_world.get_current_ball_position() == game_world.get_new_ball_position():
                # the ball hasn't moved so someone has scored
                player_in_position = game_world.get_player_at_position(
                    game_world.the_ball.current_position)
                print("{} has missed the return!".format(
                    player_in_position.name))
                print("Score is {} {}".format(
                    game_world.home_score, game_world.away_score))
            else:
                player_in_position = game_world.get_player_at_position(
                    game_world.get_current_ball_position())
                print("{} has {}!".format(player_in_position.name,
                                          random.choice(self.return_text)))

        position = 12
        for x in range(0, 4):
            if x == 2:
                print("------------------")
                print("xxxxxxxxxxxxxxxxxx")
                print("------------------")
            else:
                print("------------------")
            for y in range(0, 3):
                if position != game_world.the_ball.current_position:
                    print("{} ".format(game_world.get_player_at_position(
                        position).surname()), end='')
                else:
                    print("x ", end='')
                position = position - 1
            print()
        print("------------------")

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
        print("Name\t\t\t| Touches\t | Mistakes\t|")
        for player in game_world.teams["home"].players:
            tabs = "\t\t"
            if len(player.name) >= 16:
                tabs = "\t"

            print("{}({}){}| {}\t\t | {}\t\t|".format(
                player.name, player.ability["defense"], tabs, player.touches, player.misses))

        print("{} team stats:".format(game_world.teams["away"].name))
        print("Name\t\t\t| Touches\t | Mistakes\t|")
        for player in game_world.teams["away"].players:
            tabs = "\t\t"
            if len(player.name) >= 16:
                tabs = "\t"

            print("{}({}){}| {}\t\t | {}\t\t|".format(
                player.name, player.ability["defense"], tabs, player.touches, player.misses))
