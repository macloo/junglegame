from sys import exit

import locations

class Engine(object):
    """
    Runs the game by moving you from one location to the next. That's
    really all it does. All actions take place in the location classes.
    """

    def play(self, starting_loc):
        locmap = locations.loc_code_map
        current_loc = locmap.get(starting_loc)
        next_loc = ""

        while True:
            if next_loc == "":
                current_loc.enter()
            elif next_loc == None:
                print "I didn't understand that."
                # exit() 
            elif len(next_loc) > 2:
                print next_loc 
            else:
                current_loc = locmap.get(next_loc)
                current_loc.enter()
            next_loc = current_loc.action()

thegame = Engine()
thegame.play('27')
