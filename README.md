Jungle Game (Python 2.7)
========================

A simple text-only Python game based on exercise 45 in Zed Shaw's free online book [Learn Python the Hard Way](http://learnpythonthehardway.org/book/).

This exercise is supposed to teach us (beginners) more about object-oriented programming concepts. In a previous exercise, we started building a game with skeleton classes provided by Zed. This time, we start from scratch and design our own text game (like Zork or Adventure). 

In ex. 43, everything was coded in a single .py file. Now, in ex. 45, we are tasked with using multiple files (modules).

## The Game

You are a biologist who needs to find a rare fruit tree in the dangerous tropical jungle and return to your starting point with a sample of the fruit intact. You can travel through 31 locations to fulfill your quest. Along the way you will need to solve a few puzzles, including how to get past some jungle predators.

## Current Status

At this point, most things do not run yet. However, you can step through a few locations, and nothing throws an error. 

In location 27 (game starting point), you can pick up and drop items. Can't do much else with them yet.

## Game History

Feb. 4, 2014 - Started the exercise. Drew game map on paper. Listed all items and locations to be used in game. Thought up puzzles and how to solve them.

Feb. 6 - Coded skeleton classes for all game locations. Made a dictionary (map) for all game locations. Made Engine class to run the game. 

Feb. 7 - Created skeleton classes for all game items. These are things that can be picked up, carried, and used. First commit to GitHub. 

Feb. 8 - Added function use_item() to Location() class. Not finished yet, but it allows the player to pick up, drop, and examine items that are found in the game. Also worked out a new function -- defaults() -- for handling directional movement from one location to another. That required a rewrite of the Engine() class.

Feb. 9 - Lots of work on taking and dropping items, carrying them to different locations, and making the raft an item that can only be carried alone, not with other items. Lots of trial and error. Reorganized functions in main Location() class.

Feb. 11 - More work on items. Now they can be put into the raft; the raft cannot be carried when things are inside it; the things can be seen if they are inside the raft. The put_items() was time-consuming.
