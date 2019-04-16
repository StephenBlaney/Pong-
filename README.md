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
```python 
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # fastest possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # fastest possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # fastest possible speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
``` 

![Part2](https://user-images.githubusercontent.com/22968181/56209021-6df30400-604a-11e9-8f14-d68f510564ac.PNG)

# Step 3: Moving the Paddles.

We will be creating our first function of our program here, we will need this to control our paddles up and down. First things first we need to define our function ``` def paddle_a_up():```  Now, we need to get the current Y Coordinate of paddle_a  ``` y  = paddle_a.ycor()``` . Ycor is from the turtle module and what it does is returns the y coordinates and we are assigning it to a variable called y. Note: Functions/ Methods in python must have four whitespaces after the function is defined otherwise you will get an indentation error. In order for this to move we need to get the current y coordinate and add by 20 pixels. This does not create the movement however, we need to set the paddle as the current version of the y coordinate (y + 20)

Now we have our function defined except it’s not being use, for our program to use our function we need to bind it to something we call keyboard binning’s. This is essentially having one of our keyboard keys activate or function to move our paddle. 

``` Wn.listen```  this line listen for keyboard input and ``` onKeypress()```  says when the w key is pressed call the ``` paddle_a_up```  method which in turn runs the code within it and there moves the paddle 20 pixels up.

Now we have our left paddle going up, so what we can do is copy that method and use it for the paddle going down except this time we set new y cord as -20 and we also need to create a key binding for that as well. Now we have the full controls working for the left paddle. Repeat for the right paddle.  





