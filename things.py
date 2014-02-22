# all things/items in the jungle game


class Thing(object):
    """
    Parent class for all things/items in the game.
    """

    def __init__(self, name, nick, description):
        self.name = name
        self.nickname = nick
        self.descrip = description


d1 = """A heavy-duty inflatable boat, fully inflated, and large
enough to carry two people safely."""
raft = Thing("raft", "raft", d1)

d2 = """A long, broad, sharp blade with a wooden handle, about
14 inches long."""
machete = Thing("machete", "machete", d2)
 
d3 = """A fancy clear-plastic container with some kind of electronics
built into the base. The name of a bioengineering company is
printed on the top."""
jar = Thing("scientific collection jar", "jar", d3)

d4 = """A plastic packet of good-quality dried meat for keeping
your energy levels up."""
jerky = Thing("packet of beef jerky", "jerky", d4)

d5 = """A long metal torch, packed with heavy D batteries.
It weighs a lot."""
flash = Thing("flashlight", "flash", d5)

d6 = """A large coil of nylon rope, suitable for rock climbing."""
rope = Thing("rope", "rope", d6)

d7 = """A sturdy plastic model from a trekking outfitter, this
will emit a piercing loud sound."""
whistle = Thing("whistle", "whistle", d7)

d8 = """A large, old-style analog device, with a glass face and
a perky needle that always points north."""
compass = Thing("compass", "compass", d8)

d9 = """A battered ancient traditional basket, wide and shallow,
woven from grass or reeds."""
basket = Thing("basket", "basket", d9)
 
d10 = """A pump, extremely ripe purple fruit; it is heavy, large,
and exudes a delicious fragrance."""
fruit = Thing("ripe bongo fruit", "fruit", d10)

things = [raft, machete, jar, jerky, flash, rope, whistle, compass,
       basket, fruit]

# for testing this file
def main(t):
    for thing in things:
        print thing.name
        print thing.nickname
        print thing.descrip
        print

if __name__ == "__main__":
    main(things)
