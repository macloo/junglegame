from sys import exit

import locations

class Engine(object):
    """
    Runs the game.
    """

    def play(self, starting_loc):
        locmap = locations.loc_code_map
        current_loc = locmap.get(starting_loc)

        while True:
            current_loc.enter()
            next_loc = current_loc.action()
            if next_loc == None:
                print "No next location given."
                exit()
            else:
                current_loc = locmap.get(next_loc)

thegame = Engine()
thegame.play('02')
