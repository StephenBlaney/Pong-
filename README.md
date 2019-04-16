# Pong
Pong is one of the earliest arcade video games. It is a table tennis sports game featuring simple two-dimensional graphics. The game was originally manufactured by Atari, which released it in 1972.

Simple pong in python 3 for beginnings by Stephen Blaney. Note this program is a fun way of teaching the basics of python programming, it does not go in to the details of object-oriented programming or classes. A way of learning while showing your friends your adaption of the biggest game to influence the gaming industry.

# Part 1: Getting started

The program will be developed using the turtle module. It’s a great little module for graphics and can be a great starting point for developing games using python. Pygame is another module that is very good for game dev but for starting off we will be using turtle. Turtle is built in to python so we do not have to install it unlike Pygame.

First thing we need to do I create our screen turtle object Note: that screen is capitalised. We than give our window a title.  We will also set the background our window to black. Next, we want to change the size of our screen to be 600 x 800.

Now the next line ```wn.tracer(0)``` actually prevents the window from updating meaning we have to manually update it. We do this in order to speed up out games.

The main game loop is going to be where all the main activity of our game will be taking place. We create a while loop and when it’s true (which it always is meaning it’s guaranteed to run) do the following actions. We start this by telling the window to update. 
Now would be a good time to run the program and what you should have is a simple black screen 800 x 600 as specified. The coordinates at the centre is 0,0 +300 is the top and -300 is the bottom +400 and -400 is right and left respectively it’s important to remember this numbers for later.

```python
import turtle

wn = turtle.Screen() #screen object
wn.title("Pong by Stephen Blaney")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Main game loop

while True:
    wn.update()
```
    
![Part1](https://user-images.githubusercontent.com/22968181/56204551-a5a87e80-603f-11e9-988c-5736b73985a6.PNG)


# Part 2: Creating our paddles and ball
Moving on we need to create our pong paddles along with the ball. We do this by creating a Turtle object that will represent these items along with their respective attributes. The following is how we create our turtle objects.

```Paddle_a = turtle.Turtle()```

NOTE: Watch the capitalisation. Capital T as that is the class name.

We set the speed of our object to 0 which is the possible speed available otherwise this game would run very slow. The colour and shape of the paddle is set to white and square respectively, like the original game. We then lift our turtle pen; we do this cause by definition turtle objects draw the objects as they are moving across the screen. ``` 
paddle_a.penup()```. Now we want our turtle to draw our paddle at a certain part of the screen being the left, we set the turtle_a to( -350, 0).

Now you may have notice when we run the program, we have a square on the left, but the original game has more of a rectangular shape. Here we need to use the ``` turtle.shapesize()```  method in order to stretch the width. The original square is 20 x 20 so we multiply by 5 to give 100 and that will be our final rectangle shape.

Now we have our first paddle done we essentially do the same thing again except make a few changes I’d recommend copy the code and make the necessary changes which I will go through now. The only change is that we need to set the goto to plus 350 as we are setting this object to the right and of course change the name of our turtle object.

Creating our ball is very similar to our paddles copy the paddle code block and rename it ball. We want to get rid of the stretch as we want the ball to be its original size and we need to set its position to the centre of the screen which of course is 0,0


![Part2](https://user-images.githubusercontent.com/22968181/56209021-6df30400-604a-11e9-8f14-d68f510564ac.PNG)






