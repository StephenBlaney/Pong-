# Pong
Pong is one of the earliest arcade video games. It is a table tennis sports game featuring simple two-dimensional graphics. The game was originally manufactured by Atari, which released it in 1972.

Simple pong in python 3 for beginnings by Stephen Blaney. Note this program is a fun way of teaching the basics of python programming, it does not go in to the details of object-oriented programming or classes. A way of learning while showing your friends your adaption of the biggest game to influence the gaming industry.

# Part 1: Getting started

The program will be developed using the turtle module. It’s a great little module for graphics and can be a great starting point for developing games using python. Pygame is another module that is very good for game dev but for starting off we will be using turtle. Turtle is built in to python so we do not have to install it unlike Pygame.

First thing we need to do I create our screen turtle object Note: that screen is capitalised. We than give our window a title.  We will also set the background our window to black. Next, we want to change the size of our screen to be 600 x 800.

Now the next line wn.tracer(0) actually prevents the window from updating meaning we have to manually update it. We do this in order to speed up out games.```wn.tracer```

The main game loop is going to be where all the main activity of our game will be taking place. We create a while loop and when it’s true (which it always is meaning it’s guaranteed to run) do the following actions. We start this by telling the window to update. 
Now would be a good time to run the program and what you should have is a simple black screen 800 x 600 as specified. The coordinates at the centre is 0,0 +300 is the top and -300 is the bottom +400 and -400 is right and left respectively it’s important to remember this numbers for later. 

