# not surprisingly, the game starts here
# locations are in a dictionary; keys are a two-digit string
# originally this was a class but I was advised to change it
# because there's no reason for it to be a class

import locations

def main(starting_loc):
    locmap = locations.loc_code_map
    current_loc = locmap.get(starting_loc)
    next_loc = ""
    
    while True:
        if next_loc == "":
            current_loc.enter()
        elif next_loc == None:
            print "I didn't understand that." 
        elif len(next_loc) > 2:
            print next_loc
        else:
            current_loc = locmap.get(next_loc)
            current_loc.enter()
        next_loc = current_loc.action()

if __name__ == "__main__":
    main('27')
