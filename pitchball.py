import random
import time
from world import World
from commentary import Commentary


HOME_TEAM_NAME = input('name your team: ')
OPP_TEAM_NAMES = ['splinter prosthetics slayers', 'catterick carnage',
                  'p. c. madrid (progreso)', 'mapbit brothers industries']
AWAY_TEAM_NAME = random.choice(OPP_TEAM_NAMES)

GAME_WORLD = World()
GAME_WORLD.generate_teams(HOME_TEAM_NAME, AWAY_TEAM_NAME)
COMMENTARY = Commentary()

COMMENTARY.intro(GAME_WORLD)

def match_start():

    match_time = 0
    print("ref blows the whistle and we're under way!")
    GAME_WORLD.choose_team_to_serve()

    while match_time < 20 or GAME_WORLD.the_ball.new_state_served:
        
        GAME_WORLD.update()

        COMMENTARY.update(GAME_WORLD)

        GAME_WORLD.swap_buffers()

        time.sleep(2)
        match_time += 1
        print("Match Time: {} {}".format(match_time,
                                         GAME_WORLD.the_ball.new_state_served))

    COMMENTARY.final_result(GAME_WORLD)

    COMMENTARY.statistics(GAME_WORLD)




match_start()
