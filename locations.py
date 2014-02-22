# all location classes for game	
# dictionary at bottom

from sys import exit
from things import *


class Location(object):
    """
    Parent class for all locations in the game. Location 00. Lots of 
    functions here because they are available in ALL locations.
    - action() is the crucial function; receives lists from main.py
    - response (variable) stores the interaction from the player
    """

    def __init__(self):
        self.items = []
        self.first_visit = True
        self.raft_launched = False
        self.arrived_from_river = False

    name = None
    descrip = None

    def enter(self):
    # announce the current location when you enter it
        print "\n", self.name
        if self.first_visit:
            print self.descrip, "\n"
            self.first_visit = False
        self.list_items()

    def action(self, c):
    # runs in all location classes - main.py makes it so 
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]
        
        t = []
        while True:
            response = raw_input("> ")
            # this is a special one-time event -
            if self.raft_launched:
                return '13', c
            # this finds out what items are available -
            elif self.items or inventory:
                t = self.check_for_things(response, c)
            if t: # if len(t) > 0
                c = self.use_item(response, t, c)
            elif "look" in response:
                print self.descrip
                self.list_items()
                self.list_raft_contents(c)
            elif "inventory" in response or response == "i":
                self.take_inventory(c)
            elif "drop" in response:
                 c = self.drop_all(response, c)
            elif "take" in response:
                print "What do you want to take?"
            elif response == "exit":
                self.exit_game()
            else:
                next_loc = self.travel(response)
                return next_loc, c
                # travel is particular to each location

    def check_for_things(self, r, c):
    # find out which and how many things you named in your response
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]

        t = []
        for item in self.items:
            if item.nickname in r:
                t.append(item)
        for item in inventory:
            if item.nickname in r:
                t.append(item)
        if raft in self.items and raft_contents:
            for item in raft_contents:
                if item.nickname in r:
                    t.append(item)
            return t
        else:
            return t

    def list_items(self):
    # announce all items available in your current location
        if self.items:
            for item in self.items:
                print "    There is a %s here" % item.name
            print

    def list_raft_contents(self, c):
    # announce all items inside the raft
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]
        
        if raft in self.items and raft_contents:
            print "Inside the raft:"
            for item in raft_contents:
                print "    a", item.name
            print

    def take_inventory(self, c):
    # lists all things that you are carrying
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]

        if inventory:
            print "You are carrying:"
            for item in inventory:
                print item.name
        else:
            print "You are not carrying anything."

    def drop_all(self, r, c):
    # runs when "drop" appears in response but no items were named 
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]
        
        if r == "drop":
            print "Drop what? Give us a hint!"
        elif "all" in r or "everything" in r:
            if inventory:
                for item in inventory:
                    print "%s dropped" % item.name
                    self.items.append(item)
                    if item.name == "raft":
                        carrying_raft = False
                inventory = []
                print
            else:
                print "You are not carrying anything."
        else:
            print "What do you want to drop?"
        
        c = [inventory, raft_contents, carrying_raft]
        return c

    def use_item(self, r, t, c):
    # This function runs if you have typed the name of ANY item in
    # your response. It handles all generic manipulations of the items  
    # in any location: put, look, drop, take
    # It will NOT run if you did not include an item name in your response.
        if "put" in r:
            c = self.put_items(r, t, c)
        elif len(t) > 1:
            print "You can only deal with one item at a time."
        elif "look" in r:
            print t[0].descrip, "\n"
        elif "drop" in r:
            c = self.drop_items(t, c)
        elif "take" in r:
            c = self.take_items(t, c)
        else:
            print "What do you want to do with the %s?" % t[0].name
        
        return c

    def put_items(self, r, t, c):
    # how to put items in the raft
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]
        
        if len(t) == 1:
            # only 1 item in response with put
            print "What do you want to put the %s into?" % t[0].name
        elif len(t) > 2:
            # more than 2 items in response with put
            print "That's too many things. Put them in one at a time."
        else:
            # find out the word order in response
            # because the order of items will otherwise be random
            words = r.split(' ')
            for i in range(0, len(words)):
                if t[0].nickname in words[i]:
                    pos_a = i
                elif t[1].nickname in words[i]:
                    pos_b = i
            if pos_a < pos_b:
                first_item = t[0].name
                second_item = t[1].name
            else:
                first_item = t[1].name
                second_item = t[0].name
            if second_item != "raft":
                print "You can't put the %s" % first_item, 
                print "into the %s." % second_item
            else:
                if carrying_raft:
                    print "You can't put anything in the raft while you",
                    print "are carrying it."
                elif t[0].name != "raft" and not t[0] in inventory:
                    print "You are not holding the %s." % t[0].name
                elif t[1].name != "raft" and not t[1] in inventory:
                    print "You are not holding the %s." % t[1].name
                else:
                    print "The %s is in the raft." % first_item
                    if t[0].name == first_item:
                        inventory.remove(t[0])
                        raft_contents.append(t[0])
                    else:
                        inventory.remove(t[1])
                        raft_contents.append(t[1])
        
        c = [inventory, raft_contents, carrying_raft]
        return c

    def drop_items(self, t, c):
    # if item is in inventory, can drop - drop_all() is separate function
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]
        
        if t[0] in inventory:
            inventory.remove(t[0])
            self.items.append(t[0])
            print "You drop the %s." % t[0].name
            # check for raft
            if t[0].name == "raft":
                carrying_raft = False
        else:
            print "You are not carrying any %s." % t[0].name
        
        c = [inventory, raft_contents, carrying_raft]
        return c

    def take_items(self, t, c):
    # how to pick up things (the raft can only be carried alone)
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]

        if t[0] in inventory:
            print "You are already carrying the %s." % t[0].name
        elif not t[0] in self.items:
            if raft in self.items:
                c = self.take_from_raft(t, c)
            else:
                print "There is no %s here." % t[0].name
        elif t[0].name == "raft":
            if inventory:
                print "You can't pick up the raft when you are",
                print "carrying other things."
            elif raft_contents:
                print "You can't pick up the raft when things",
                print "are in it."
            else:
                carrying_raft = True
                c = self.relocate_item(t, c)       
        else:
            c = self.check_inventory(t, c)
        
        c = [inventory, raft_contents, carrying_raft]
        return c

    def take_from_raft(self, t, c):
    # take items out of raft
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]

        if not t[0] in raft_contents:
            print "There is no %s here." % t[0].name
        else:
            c = self.check_inventory(t, c)
        
        c = [inventory, raft_contents, carrying_raft]
        return c

    def check_inventory(self, t, c):
    # are you carrying more than 4 items? or carrying the raft?
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]
        
        if len(inventory) < 4:
            if carrying_raft:
                print "You can't carry anything else when you are carrying",
                print "the raft."
            else:
                c = self.relocate_item(t, c)
        else:
            print "You cannot take the %s." % t[0].name
            print "You are carrying too many things already."
            print 'Type "inventory" or "i" to see what you\'ve got.\n'
        
        c = [inventory, raft_contents, carrying_raft]
        return c

    def relocate_item(self, t, c):
    # remove item from a list and add it to your inventory list
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]
        
        inventory.append(t[0])
        if t[0] in self.items:
            self.items.remove(t[0])
        elif t[0] in raft_contents:
            raft_contents.remove(t[0])
        print "You are now carrying the %s." % t[0].name
        
        c = [inventory, raft_contents, carrying_raft]
        return c

    def exit_game(self):
        a = raw_input("Do you want to quit the game? y/n ")
        if a == "y":
            exit()


class Bongo_Glade(Location):
    """
    Location 01. Fruit, in tree, is here.
    """

    name = "Glade of the Bongo Fruit Tree"
    descrip = """    Sunlight streams down from a wide opening in the
    forest canopy. Directly below that opening stands a 
    magnificent stout tree, its branches bending with the 
    weight of large, round, shining purple fruits. There 
    is a break in the dense forest to the south."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You can't go that way."
        elif "east" in r or r == 'e':
            return "You can't go that way."
        elif "south" in r or r == 's':
            return '07'
        elif "west" in r or r == 'w':
            return "You can't go that way."
        else:
            return None


class Path2(Location):
    """
    Location 02.
    """

    name = "Path"
    descrip = """    The remains of a cleared path run east and south. To 
    the east is a kind of bridge."""   

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You can't go that way."
        elif "east" in r or r == 'e':
            return '03'
        elif "south" in r or r == 's':
            return '08'
        elif "west" in r or r == 'w':
            return "You can't go that way."
        else:
            return None


class North_Bridge(Location):
    """
    Location 03.
    """

    name = "Bridge"
    descrip = """    A rickety structure made only of bamboo strips and 
    woven rattan spans the river. Standing on this bridge is
    surely a great risk!"""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You can't go that way."
        elif "east" in r or r == 'e':
            return '04'
        elif "south" in r or r == 's':
            return "You can't go that way."
        elif "west" in r or r == 'w':
            return '02'
        else:
            return None


class Path4(Location):
    """
    Location 04.
    """

    name = "Path"
    descrip = """    Here a barely perceptible old path leads to the 
    south and east. A kind of bridge can be seen to the west."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You can't go that way."
        elif "east" in r or r == 'e':
            return '05'
        elif "south" in r or r == 's':
            return '09'
        elif "west" in r or r == 'w':
            return '03'
        else:
            return None


class Path5(Location):
    """
    Location 05. Dead end.
    """

    def __init__(self):
        self.first_visit = True
        self.items = [basket]
        self.raft_launched = False
        self.arrived_from_river = False

    name = "Path"
    descrip = """    The path ends here, choked off by dense foliage
    and thick, twisted vines. An ancient basket, woven from 
    grasses or reeds, lies on the ground."""
    descrip2 = """    The path ends here, choked off by dense foliage
    and thick, twisted vines."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You can't go that way."
        elif "east" in r or r == 'e':
            return "You can't go that way."
        elif "south" in r or r == 's':
            return "You can't go that way."
        elif "west" in r or r == 'w':
            return '04'
        else:
            return None


class Dense_Forest6(Location):
    """
    Location 06. Dead end.
    """

    name = "Dense Forest"
    descrip = """    The forest growth is impossibly thick here. You can
    only return the way you came. A delicious fruity smell 
    fills the air."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You can't go that way."
        elif "east" in r or r == 'e':
            return '07'
        elif "south" in r or r == 's':
            return "You can't go that way."
        elif "west" in r or r == 'w':
            return "You can't go that way."
        else:
            return None


class Dense_Forest7(Location):
    """
    Location 07. Here you must hack through with the machete.
    """

    name = "Dense Forest"
    descrip = """    The tangled undergrowth here might yield to a sharp
    blade. At present, you can't go anywhere but east."""
    descrip2 = """    Someone has hacked away at the tangled undergrowth 
    here, opening a way to the north. You can also go east or west."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '01'
        elif "east" in r or r == 'e':
            return '08'
        elif "south" in r or r == 's':
            return "You can't go that way."
        elif "west" in r or r == 'w':
            return '06'
        elif "southwest" in r or r == 'sw':
            return '11'
        else:
            return None


class Slope(Location):
    """
    Location 08.
    """

    name = "Small Slope"
    descrip = """    The ground here makes a hump, going up toward the west.
    You could move sideways on the slope toward the north."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '02'
        elif "east" in r or r == 'e':
            return "You can't go that way."
        elif "south" in r or r == 's':
            return "You can't go that way."
        elif "west" in r or r == 'w':
            return '07'
        else:
            return None


class Dense_Forest9(Location):
    """
    Location 09.
    """

    name = "Dense Forest"
    descrip = """    The forest growth here is very thick, and the
    canopy far overhead makes your surroundings rather dark.
    In some places, bars of bright sunlight break through the
    trees and create little puddles of brilliant green on the
    forest floor."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '04'
        elif "east" in r or r == 'e':
            return "You can't go that way."
        elif "south" in r or r == 's':
            return "You can't go that way."
        elif "west" in r or r == 'w':
            return "You can't go that way."
        elif "southeast" in r or r == 'se':
            return '14'
        else:
            return None


class Falls(Location):
    """
    Location 10. Here you die.
    """

    name = "Falls"
    descrip = """    You are swept over the edge of the falls!\n 
    It's a long
               long
                   long
                        way
                        down ...\n
    Goodbye!"""

    def action(self, c):
        exit()


class Panther_Forest(Location):
    """
    Location 11. Here you must survive the panther.
    """

    name = "Forest"
    descrip = """    A few openings lead out from here: north, south,
    and possibly east. A large black panther stretches out
    along a thick tree branch just above your head.
    
    The panther appears to be sleeping.""" 

    def travel(self, r):
        if "north" in r or r == 'n':
            return '07'
        elif "east" in r or r == 'e':
            return '12'
        elif "south" in r or r == 's':
            return '15'
        elif "west" in r or r == 'w':
            return "You can't go that way."
        else:
            return None


class Dense_Forest12(Location):
    """
    Location 12.
    """

    name = "Dense Forest"
    descrip = """    The jungle lies hot and still all around you.
    Some chirps and twitters can be heard, but perhaps even
    the usual inhabitants of this place are subdued by the
    heat and humidity."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You can't go that way."
        elif "east" in r or r == 'e':
            return "The river is there."
        elif "south" in r or r == 's':
            return '16'
        elif "west" in r or r == 'w':
            return '11'
        else:
            return None


class North_River(Location):
    """
    Location 13. Here you must land the raft.
    """

    def __init__(self):
        self.first_visit = True
        self.raft_launched = False
        self.arrived_from_river = False
        
        # the raft must be here, or else YOU would not be here 
        self.items = [raft] 

    name = "River"
    descrip = """    The water gets rougher and faster. You see a possible
    landing place to the right and a high bank to the left.
    Realizing that you do not have a paddle, you consider
    that maybe by leaning hard and pulling on the front side
    of the raft, you might be able to steer it."""

    def use_item(self, r, t, c):
    # special version of this function because you are in a dire situation!
        if len(t) > 1:
            print "You can only deal with one item at a time."
        elif "look" in r:
            print t[0].descrip, "\n"
        elif t[0].name == "raft":
            print "Where do you want to steer the raft?"
        elif "drop" in r:
            print "If you drop the %s now, it will be gone forever!" % t[0].name 
        else:
            print "This is no time to be fooling around with the",
            print "%s!" % t[0].name
        return c

    def travel(self, r):
        if "right" in r or ("east" in r or r == 'e'):
            # take raft with you to the landing site - 
            self.items.remove(raft)
            # inventory.append(raft)
            self.arrived_from_river = True
            return '14'
        else:
            return '10'


class Clearing14(Location):
    """
    Location 14. Here is where the raft lands.
    """

    def __init__(self):
        self.first_visit = True
        self.raft_launched = False
        self.arrived_from_river = True
        self.items = []
        
    name = "Clearing"
    descrip = """    A sandy, flat space makes a safe landing area
    beside the rushing river. A narrow track cuts north and west."""

    def enter(self):
    # special version of this for this location
        print self.name
        if self.arrived_from_river:
            self.items.append(raft)
            self.arrived_from_river = False
        if self.first_visit:
            print self.descrip
            self.first_visit = False
        self.list_items()

    def travel(self, r):
        if "north" in r or r == 'n':
            return "There's no passage that way."
        elif "east" in r or r == 'e':
            return "Dense jungle blocks that side of the clearing."
        elif "south" in r or r == 's':
            return "Dense jungle blocks that side of the clearing."
        elif "west" in r or r == 'w':
            a = "If you went into the river here, you would be swept \n"
            b = "over the falls to your doom."
            return a + b
        if "northwest" in r or r == 'nw':
            return '09'
        else:
            return None


class Dense_Forest15(Location):
    """
    Location 15.
    """

    name = "Dense Forest"
    descrip = """    The stillness of the forest is almost eerie.
    Every step you take makes a dull sound, crunching twigs
    and leaves and who-knows-what under your boots."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '11'
        elif "east" in r or r == 'e':
            return "You can't go that way."
        elif "south" in r or r == 's':
            return '17'
        elif "west" in r or r == 'w':
            return "You can't go that way."
        else:
            return None


class Path16(Location):
    """
    Location 16.
    """

    name = "Path"
    descrip = """    The way is clear to the north and to the south."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '12'
        elif "east" in r or r == 'e':
            return "The river is there."
        elif "south" in r or r == 's':
            return '18'
        elif "west" in r or r == 'w':
            return "You can't go that way."
        else:
            return None


class Dense_Forest17(Location):
    """
    Location 17.
    """

    name = "Dense Forest"
    descrip = """    Even though the forest floor is relatively clear,   
    walking is very tiring. The moist heat seems to drain your
    strength away step by step. And then there are the leeches.
    Just don't think about them."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '15'
        elif "east" in r or r == 'e':
            return '18'
        elif "south" in r or r == 's':
            return "You can't go that way."
        elif "west" in r or r == 'w':
            return "You can't go that way."
        else:
            return None


class Path18(Location):
    """
    Location 18.
    """

    name = "Path"
    descrip = """    Here it seems a path has been worn away, but   
    it disappears to the west and south. The path continues
    to the north."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '16'
        elif "east" in r or r == 'e':
            return "The river is there."
        elif "south" in r or r == 's':
            return '21'
        elif "west" in r or r == 'w':
            return '17'
        else:
            return None


class Log_Forest(Location):
    """
    Location 19. Here you can pick up a log.
    """

    name = "Forest"
    descrip = """    A great Dryobalanops tree, maybe 80 meters tall,
    has crashed down here, bringing with it several smaller
    trees. They lie in a jumble, tangled in vines and lianas.
    A clearing opens to the east and southeast."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You can't go that way."
        elif "east" in r or r == 'e':
            return '20'
        elif "south" in r or r == 's':
            return "You can't go that way."
        elif "west" in r or r == 'w':
            return "You can't go that way."
        elif "southeast" in r or r == 'se':
            return '24'
        else:
            return None


class Clearing20(Location):
    """
    Location 20.
    """

    name = "Clearing"
    descrip = """    Sun streams into this open space, making it quite   
    hot, but not quite as dense and wet as under the trees.
    You can breathe more easily here. A huge fallen tree is
    visible to the west. A swampy area lies south."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You can't go that way."
        elif "east" in r or r == 'e':
            return "You can't go that way."
        elif "south" in r or r == 's':
            return '22'
        elif "west" in r or r == 'w':
            return '19'
        else:
            return None


class Viper_Forest(Location):
    """
    Location 21. Here you must survive the pit viper.
    """

    name = "Forest"
    descrip = """    The path continues north and south here, but 
    dangling from a low branch right in front of you, a
    pit viper flicks its forked tongue in and out, staring
    straight into your eyes!"""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '18'
        elif "east" in r or r == 'e':
            return "You can't go that way."
        elif "south" in r or r == 's':
            return '23'
        elif "west" in r or r == 'w':
            return "You can't go that way."
        else:
            return None


class Swamp(Location):
    """
    Location 22. This swamp is hard to cross.
    """

    name = "Swamp"
    descrip = """    This swamp at first seems to be gloppy mud that   
    could be crossed. (Thank goodness you are wearing sturdy 
    boots!)"""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '20'
        elif "east" in r or r == 'e':
            return '23'
        elif "south" in r or r == 's':
            return '24'
        elif "west" in r or r == 'w':
            return "You can't go that way."
        else:
            return None


class Path23(Location):
    """
    Location 23.
    """

    name = "Path"
    descrip = """    Here it seems a path has been worn away, but   
    it disappears to the west. The path continues to the north."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '21'
        elif "east" in r or r == 'e':
            return "You can't go that way."
        elif "south" in r or r == 's':
            return "You can't go that way."
        elif "west" in r or r == 'w':
            return '22'
        else:
            return None


class Clearing24(Location):
    """
    Location 24.
    """

    name = "Clearing"
    descrip = """    Sun streams into this open space, making it quite   
    hot, but not quite as dense and wet as under the trees.
    You can breathe more easily here. A swampy area lies 
    north. The forest might be passable to the northwest 
    and east."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '22'
        elif "east" in r or r == 'e':
            return '25'
        elif "south" in r or r == 's':
            return "You can't go that way."
        elif "west" in r or r == 'w':
            return "You can't go that way."
        elif "northwest" in r or r == 'nw':
            return '19'
        else:
            return None


class Dense_Forest25(Location):
    """
    Location 25. Here you must hack through with the machete.
    """

    name = "Dense Forest"
    descrip = """    There is an opening to the west here, but in all
    other directions, the thick jungle blocks your way."""
    descrip2 = """    A narrow path has been hacked through the dense
    undergrowth here, leading south. There is an opening
    to the west."""

    def __init__(self):
        self.items = [] 
        self.first_visit = True
        self.blocked = True
        self.raft_launched = False

    def use_item(self, r, t, c):
    # we have a special version of this function in this location 
    # because the machete can be used here
        if "put" in r:
            c = self.put_items(r, t, c)
        elif len(t) > 1:
            print "You can only deal with one item at a time."
        elif "look" in r:
            print t[0].descrip, "\n"
        elif "drop" in r:
            c = self.drop_items(t, c)
        elif "take" in r:
            c = self.take_items(t, c)
        elif t[0].name == "machete":
            verbs = ["cut", "hack", "slash", "slice", "chop"]
            for verb in verbs:
                if verb in r:
                    print "You %s through the thick foliage with the" % verb
                    print "machete and open a new path to the south."
                    self.blocked = False
                    self.descrip = self.descrip2
                    break
        else:
            print "What do you want to do with the %s?" % t[0].name
        
        return c

    def travel(self, r):
        if "north" in r or r == 'n':
            return "The forest is too thick. That way is impassable."
        elif "east" in r or r == 'e':
            return "You cannot enter the river here."
        elif "south" in r or r == 's':
            if self.blocked:
                a = "If only you had some way to cut through the dense jungle!"
                return a
            else:
                return '29'
        elif "west" in r or r == 'w':
            return '24'
        else:
            return None


class South_River(Location):
    """
    Location 26. Here you can launch the raft.
    """

    name = "River"
    descrip = """    This wide, unnamed river is deep and hazardous. The 
    far bank lies to the west of where you stand. This is one 
    of the relatively few rivers in the world that flow north.
    You are on the east bank."""

    def use_item(self, r, t, c):
    # we have a special version of this function in this location 
    # because the raft can be launched into the river here
        # unpack collections
        inventory = c[0]
        raft_contents = c[1]
        carrying_raft = c[2]
        
        if "put" in r:
            c = self.put_items(r, t, c)
        elif len(t) > 1:
            print "You can only deal with one item at a time."
        elif "look" in r:
            print t[0].descrip, "\n"
        elif "drop" in r:
            c = self.drop_items(t, c)
        elif "take" in r:
            c = self.take_items(t, c)
        elif t[0].name == "raft":
            verbs = ["drag", "float", "launch", "pull", "push"]
            
            a = "You manage to drag the raft into the river, keeping it from \n"
            a += "floating away until you carefully step into it, crouch "
            a += "down, \n"
            a += "and sit steadily in the center. By leaning forward with a \n"
            a += "small lurch, you launch the raft into the current!\n"

            for verb in verbs:
                if (verb in r) and (raft in self.items):
                    self.raft_launched = True
                    self.items.remove(raft)
                    print a
                    break
                elif (verb in r) and (raft in inventory):
                    print "The raft should be on the ground to do that."
                    break
        else:
            print "What do you want to do with the %s?" % t[0].name
        return c

    def travel(self, r):
        if "river" in r or ("north" in r or r == 'n'):
            return "You can only go downriver if you use the raft."
        elif "east" in r or r == 'e':
            return '27'
        elif "south" in r or r == 's':
            return "You cannot go upriver. The current is too swift."
        elif "west" in r or r == 'w':
            a = "It is impossible to cross to the west bank of the river here."
            return a
        else:
            return None


class Vehicle_Clearing(Location):
    """
    Location 27. This is where the game always begins.
    """

    def __init__(self):
        self.first_visit = True
        self.raft_launched = False
        
        self.items = [raft, machete, jar, jerky, flash, rope, whistle, 
                   compass]

    name = "Clearing"
    descrip = """    Your vehicle, a powerful but compact 4WD, is parked in
    a broad clearing at the end of a dirt track, which 
    disappears into the jungle to the north. A wide river 
    lies in front of you. The clearing extends to the south."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '28'
        elif "east" in r or r == 'e':
            return "You can't go that way."
        elif "south" in r or r == 's':
            return '31'
        elif "river" in r or ("west" in r or r == 'w'):
            return '26'
        else:
            return None


class Dirt_Road(Location):
    """
    Location 28. Dead end.
    """

    name = "Dirt Road"
    descrip = """    This narrow, partly overgrown track extends straight 
    ahead into the jungle. This is the road that brought you
    to this lonely place, where you hope to find the greatest
    scientific discovery of your career."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You came from that direction in your 4WD."
        elif "east" in r or r == 'e':
            return "A deep ravine blocks your way."
        elif "south" in r or r == 's':
            return '27'
        elif "west" in r or r == 'w':
            a = "You can hear the river, but the forest growth is too thick.\n"
            b = "It's impossible to break through in that direction."
            return a + b
        else:
            return None


class Dense_Forest29(Location):
    """
    Location 29. Here you must hack your way through with the machete.
    """

    def __init__(self):
        self.items = [] 
        self.first_visit = True
        self.blocked = True
        self.raft_launched = False

    name = "Dense Forest"
    descrip = """    The forest floor is choked with twisted undergrowth,
    and tall thorny plants bar the way between the trees.
    A bridge lies to the east."""
    descrip2 = """    A narrow path has been hacked through the thorny
    undergrowth here. A bridge lies to the east."""

    def use_item(self, r, t, c):
    # we have a special version of this function in this location 
    # because the machete can be used here        
        if "put" in r:
            c = self.put_items(r, t, c)
        elif len(t) > 1:
            print "You can only deal with one item at a time."
        elif "look" in r:
            print t[0].descrip, "\n"
        elif "drop" in r:
            c = self.drop_items(t, c)
        elif "take" in r:
            c = self.take_items(t, c)
        elif t[0].name == "machete":
            verbs = ["cut", "hack", "slash", "slice", "chop"]
            for verb in verbs:
                if verb in r:
                    print "You %s through the tough branches with the" % verb
                    print "machete and clear a pathway to the north."
                    self.blocked = False
                    self.descrip = self.descrip2
                    break
        else:
            print "What do you want to do with the %s?" % t[0].name
        return c

    def travel(self, r):
        if "north" in r or r == 'n':
            if self.blocked:
                a = "If only you had some way to cut through the thorny "
                b = "branches!"
                return a + b
            else:
                return '25'
        elif "east" in r or r == 'e':
                return '30'
        elif "south" in r or r == 's':
            return "There is no way through in that direction."
        elif "west" in r or r == 'w':
            return "It is impossible to go in that direction."
        else:
            return None
 

class South_Bridge(Location):
    """
    Location 30.
    """

    name = "Log Bridge"
    descrip = """    This bridge (if you can call it a bridge) consists of   
    one very long log and a kind of rope made from twisted plant 
    fibers or thin vines. Moss covers the log, which is rather 
    narrow. The rope is strung between two upright trees so 
    you can hold on to it while crossing."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "If you went that way, you would be in the river."
        elif "east" in r or r == 'e':
            return '31'
        elif "south" in r or r == 's':
            return "If you went that way, you would be in the river."
        elif "west" in r or r == 'w':
            print "Holding very tightly to the rope that stretches across"
            print "the swift river, you manage to walk across the slippery"
            print "narrow log to the opposite side."
            return '29'
        else:
            return None


class Clearing31(Location):
    """
    Location 31.
    """

    name = "Clearing"
    descrip = """    A small open space is hemmed in by jungle on all sides. 
    You can see your 4WD vehicle to the north. A bridge 
    lies to the west."""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '27'
        elif "east" in r or r == 'e':
            return "A deep ravine blocks your way."
        elif "south" in r or r == 's':
            return "The jungle is much too dense in that direction."
        elif "west" in r or r == 'w':
            return '30'
        else:
            return None


# dictionary for all locations 
loc_code_map = {
       '01': Bongo_Glade(),
       '14': Clearing14(),
       '20': Clearing20(),
       '24': Clearing24(),
       '31': Clearing31(),
       '12': Dense_Forest12(),
       '15': Dense_Forest15(),
       '17': Dense_Forest17(),
       '25': Dense_Forest25(),
       '29': Dense_Forest29(),
       '06': Dense_Forest6(),
       '07': Dense_Forest7(),
       '09': Dense_Forest9(),
       '28': Dirt_Road(),
       '10': Falls(),
       '00': Location(),
       '19': Log_Forest(),
       '03': North_Bridge(),
       '13': North_River(),
       '11': Panther_Forest(),
       '16': Path16(),
       '18': Path18(),
       '02': Path2(),
       '23': Path23(),
       '04': Path4(),
       '05': Path5(),
       '08': Slope(),
       '30': South_Bridge(),
       '26': South_River(),
       '22': Swamp(),
       '27': Vehicle_Clearing(),
       '21': Viper_Forest()
       }

# for testing this file
def main(m):
    for key, val in m.items():
        cur_loc = m.get(key)
        cur_loc.enter()

if __name__ == "__main__":
    main(loc_code_map)
