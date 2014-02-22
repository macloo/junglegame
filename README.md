Jungle Game (Python 2.7)
========================

A simple text-only Python game based on [exercise 45](http://learnpythonthehardway.org/book/ex45.html) in Zed Shaw's free online book [Learn Python the Hard Way](http://learnpythonthehardway.org/book/).

This exercise is supposed to teach us (beginners) more about object-oriented programming concepts. In a previous exercise (43), we started building [a game](https://github.com/macloo/pythongame) with skeleton classes provided by Zed. This time, we start from scratch and design our own text game (like [Zork](http://en.wikipedia.org/wiki/Zork) or [Adventure](http://en.wikipedia.org/wiki/Colossal_Cave_Adventure)). 

In ex. 43, everything was coded in a single .py file. Now, in ex. 45, we are tasked with using multiple files (modules).

This has been a GREAT learning exercise for working with objects. I had never understood OOP until three weeks before I began this exercise. Now I understand a lot more. (Probably I am still doing many things wrong.)

Granted, this is only a simple game, but in working with variables, lists, and functions in this game, I've learned a ton about how to traverse the classes in my code.

## The Game

You are a biologist who needs to find a rare fruit tree in the dangerous tropical jungle and return to your starting point with a sample of the fruit intact. You can travel through 31 locations to fulfill your quest. Along the way you will need to solve a few puzzles, including how to get past some jungle predators.

## Current Status

At this point, most "adventures" do not run yet. You can go everywhere without impediments. However, you can:

* Visit all 31 locations, and nothing throws an error.
* Ride the raft down the river.
* Pick up and drop any item.
* Carry items to other locations, drop them there, and pick them up later.
* Put items into the raft and take them out again.

Gameplay:

* To run the game: python main.py
* Moving from place to place: n, e, s, and w work in most locations. Sometimes you can use other words too, as suggested by the location description. 
* You can quit cleanly by typing: exit

## Issues

Biggest issue right now is at location 14. Dealing with raft there.

travel() - Not passing c to this function. I might have to do that.

## Game History

Feb. 4, 2014 - Started the exercise. Drew game map on paper. Listed all items and locations to be used in game. Thought up puzzles and how to solve them.

Feb. 6 - Coded skeleton classes for all game locations. Made a dictionary (map) for all game locations. Made Engine class to run the game. 

Feb. 7 - Created skeleton classes for all game items. These are things that can be picked up, carried, and used. First commit to GitHub. 

Feb. 8 - Added function use_item() to Location() class. Not finished yet, but it allows the player to pick up, drop, and examine items that are found in the game. Also worked out a new function -- defaults() -- for handling directional movement from one location to another. That required a rewrite of the Engine() class.

Feb. 9 - Lots of work on taking and dropping items, carrying them to different locations, and making the raft an item that can only be carried alone, not with other items. Lots of trial and error. Reorganized functions in main Location() class. Changed defaults() to travel() -- this function, unique to each location, handles moving you out to an adjacent location. 

Feb. 11 - More work on items. Now they can be put into the raft; the raft cannot be carried when things are inside it; the things can be seen if they are inside the raft. The put_items() function was time-consuming.

Feb. 12 - Zed says spend a week on this. My week is up. However, before I return to Zed's exercise 45, I want to get the raft into the water. I've got walkthrough capability for all scenes (some do not have descriptions written) and all objects can be picked up, carried, dropped, or put into the raft. Items can be taken out of the raft. The machete can be used in two locations.

Feb. 13 - The raft works now. You can launch it, with or without items inside it. You travel downriver automatically, entering a new location no matter what you do. Then you either die or land safely, depending on your response. The raft lands with you, with all items inside (if they were inside when you launched the raft). Learned more about passing objects into other objects. Possibly inefficient solution to moving the raft downriver.

Feb. 22 - After a long break, I felt ready to tackle some suggestions I got from people on reddit who looked at this. One was to remove the class from main.py and just make it a normal function instead. Another was to get rid of all classes except one for the things in the game (raft, machete, etc.) and just make them instances of the Thing() class. Finally, and most horrible, was eliminating all the global variables. Well, there were not so many, but tracking the inventory list was a nightmare. Probably my solution is quite stupid, since it led to lots of redundancy. But I now have NO global variables, and I think I can still do everything I could do before. At least, everything I have thought of and tested does run without errors. This took several hours.

