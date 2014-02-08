# all thing classes for game

inventory = []

raft_contents = []

class Thing(object):
    """
    Parent class for all things in the game.
    """

    def __init__(self):
        self.carried = False
        self.in_raft = False


class Raft(Thing):

    name = "raft"
    nickname = name
    descrip = """A heavy-duty inflatable boat, fully inflated, and 
large enough to carry two people safely."""


class Machete(Thing):

    name = "machete"
    nickname = name
    descrip = """A long, broad, sharp blade with a wooden handle, 
about 14 inches long."""


class Sample_Jar(Thing):

    name = "scientific collection jar"
    nickname = "jar"
    descrip = """A fancy clear plastic container with some kind of 
electronics built into the base. The name of a bioengineering company 
is printed on the top."""


class Beef_Jerky(Thing):

    name = "packet of beef jerky"
    nickname = "jerky"
    descrip = """A plastic packet of good-quality dried meat for 
keeping your energy levels up."""


class Flashlight(Thing):

    name = "flashlight"
    nickname = "flash"
    descrip = """A long metal torch, packed with heavy D batteries. 
It weighs a lot."""


class Rope(Thing):

    name = "rope"
    nickname = name
    descrip = """A large coil of nylon rope, suitable for rock 
climbing."""


class Whistle(Thing):

    name = "whistle"
    nickname = name
    descrip = """A sturdy plastic model from a trekking outfitter, 
this will emit a piercing loud sound."""


class Compass(Thing):

    name = "compass"
    nickname = name
    descrip = """A large, old-style analog device, with a glass face 
and a perky needle that always points north."""


class Basket(Thing):
    """
    This is found in location 5.
    """
    name = "basket"
    nickname = name
    descrip = """A battered ancient traditional basket, wide and 
shallow, woven from grass or reeds."""


