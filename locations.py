# all location classes for game

import things

class Location(object):
    """
    Parent class for all locations in the game. Location 00.
    """

    def __init__(self):
        self.items = []

    def enter(self):
        print self.name
        print self.descrip
        if self.items:
            for item in self.items:
                print "There is a %s here\n" % item

class Bongo_Glade(Location):
    """
    Location 01.
    """

    name = "\nGlade of the Bongo Fruit Tree"
    descrip = """    Sunlight streams down from a wide opening in the
    forest canopy. Directly below that opening stands a 
    magnificent stout tree, its branches bending with the 
    weight of large, round, shining purple fruits. There 
    is a break in the dense forest to the south.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "south" in response or response == 's':
                return '07'
            else:
                print "I don't understand that."


class Path2(Location):
    """
    Location 02.
    """

    name = "\nPath"
    descrip = """    The remains of a cleared path run east and south. To 
    the east is a kind of bridge.\n"""   

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "east" in response or response == 'e':
                return '03'
            elif "south" in response or response == 's':
                return '08'
            else:
                print "I don't understand that."


class North_Bridge(Location):
    """
    Location 03.
    """

    name = "\nBridge"
    descrip = """    A rickety structure made only of bamboo strips and 
    woven rattan spans the river. Standing on this bridge is
    surely a great risk!\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "east" in response or response == 'e':
                return '04'
            elif "west" in response or response == 'w':
                return '02'
            else:
                print "I don't understand that."


class Path4(Location):
    """
    Location 04.
    """

    name = "\nPath"
    descrip = """    Here a barely perceptible old path leads to the 
    south and west. A kind of bridge can be seen to the west.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "east" in response or response == 'e':
                return '05'
            elif "west" in response or response == 'w':
                return '03'
            elif "south" in response or response == 's':
                return '09'
            else:
                print "I don't understand that."


class Path5(Location):
    """
    Location 05.
    """

    def __init__(self):
        self.basket = things.Basket()

        self.items = [self.basket.name]

    name = "\nPath"
    descrip = """    The path ends here, choked off by dense foliage
    and thick, twisted vines. An ancient basket, woven from 
    grasses or reeds, lies on the ground.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "west" in response or response == 'w':
                return '04'
            else:
                print "I don't understand that."


class Dense_Forest6(Location):
    """
    Location 06.
    """

    name = "\nDense Forest"
    descrip = """    The forest growth is impossibly thick here. You can
    only return the way you came.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "east" in response or response == 'e':
                return '07'
            else:
                print "I don't understand that."


class Dense_Forest7(Location):
    """
    Location 07.
    """

    name = "\nDense Forest"
    descrip = """    The tangled undergrowth here might yield to a sharp
    blade. At present, you can't go anywhere but east.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "east" in response or response == 'e':
                return '08'
            elif "north" in response or response == 'n':
                return '01'
            elif "west" in response or response == 'w':
                return '06'
            elif "southwest" in response or response == 'sw':
                return '11'
            else:
                print "I don't understand that."


class Slope(Location):
    """
    Location 08.
    """

    name = "\nSmall Slope"
    descrip = """    The ground here makes a hump, going up toward the west.
    You could move sideways on the slope toward the north.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "west" in response or response == 'w':
                return '07'
            elif "north" in response or response == 'n':
                return '02'
            else:
                print "I don't understand that."


class Dense_Forest9(Location):
    """
    Location 09.
    """

    name = "Dense Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Falls(Location):
    """
    Location 10.
    """

    name = "Falls"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Panther_Forest(Location):
    """
    Location 11.
    """

    name = "Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Dense_Forest12(Location):
    """
    Location 12.
    """

    name = "Dense Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class North_River(Location):
    """
    Location 13.
    """

    name = "River"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Clearing14(Location):
    """
    Location 14.
    """

    name = "Clearing"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Dense_Forest15(Location):
    """
    Location 15.
    """

    name = "Dense Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Path16(Location):
    """
    Location 16.
    """

    name = "Path"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Dense_Forest17(Location):
    """
    Location 17.
    """

    name = "Dense Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Path18(Location):
    """
    Location 18.
    """

    name = "Path"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Log_Forest(Location):
    """
    Location 19.
    """

    name = "Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Clearing20(Location):
    """
    Location 20.
    """

    name = "Clearing"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Viper_Forest(Location):
    """
    Location 21.
    """

    name = "Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Swamp(Location):
    """
    Location 22.
    """

    name = "Swamp"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Path23(Location):
    """
    Location 23.
    """

    name = "Path"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Clearing24(Location):
    """
    Location 24.
    """

    name = "Clearing"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Dense_Forest25(Location):
    """
    Location 25.
    """

    name = "Dense Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class South_River(Location):
    """
    Location 26.
    """

    name = "River"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Vehicle_Clearing(Location):
    """
    Location 27.
    """

    def __init__(self):
        self.raft = things.Raft()
        self.machete = things.Machete()
        self.jar = things.Sample_Jar()
        self.jerky = things.Beef_Jerky()
        self.flash = things.Flashlight()
        self.rope = things.Rope()
        self.whistle = things.Whistle()
        self.compass = things.Compass()
        
        self.items = [self.raft.name, self.machete.name, self.jar.name, 
                   self.jerky.name, self.flash.name, self.rope.name, 
                   self.whistle.name, self.compass.name]

    name = "\nClearing"
    descrip = """    Your vehicle, a powerful but compact 4WD, is parked in
    a broad clearing at the end of a dirt track, which 
    disappears into the jungle to the north. A wide river 
    lies in front of you. The clearing extends to the south.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "north" in response or response == 'n':
                return '28'
            elif "river" in response or ("west" in response or response == 'w'):
                return '26'
            elif "south" in response or response == 's':
                return '31'
            else:
                print "I don't understand that."


class Dirt_Road(Location):
    """
    Location 28.
    """

    name = "Dirt Road"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Dense_Forest29(Location):
    """
    Location 29.
    """

    name = ""
    descrip = """    The   
    There is """

    def action(self):
        pass


class South_Bridge(Location):
    """
    Location 30.
    """

    name = "Bridge"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Clearing31(Location):
    """
    Location 31.
    """

    name = "Clearing"
    descrip = """    The   
    There is """

    def action(self):
        pass

# dictionary for all locations 
loc_code_map = {
       '01' : Bongo_Glade(),
       '14' : Clearing14(),
       '20' : Clearing20(),
       '24' : Clearing24(),
       '31' : Clearing31(),
       '12' : Dense_Forest12(),
       '15' : Dense_Forest15(),
       '17' : Dense_Forest17(),
       '25' : Dense_Forest25(),
       '29' : Dense_Forest29(),
       '06' : Dense_Forest6(),
       '07' : Dense_Forest7(),
       '09' : Dense_Forest9(),
       '28' : Dirt_Road(),
       '10' : Falls(),
       '00' : Location(),
       '19' : Log_Forest(),
       '03' : North_Bridge(),
       '13' : North_River(),
       '11' : Panther_Forest(),
       '16' : Path16(),
       '18' : Path18(),
       '02' : Path2(),
       '23' : Path23(),
       '04' : Path4(),
       '05' : Path5(),
       '08' : Slope(),
       '30' : South_Bridge(),
       '26' : South_River(),
       '22' : Swamp(),
       '27' : Vehicle_Clearing(),
       '21' : Viper_Forest()
       }
