# Simple Pong in python 3 for beginners
# by @Stephen Blaney

# Part 1 : Getting Started

import turtle

wn = turtle.Screen() # screen object
wn.title("Pong by Stephen Blaney")
wn.bgcolor("black")
wn.setup(width=800, height=600)

#Part : Creating our

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


# Main game loop

while True:
    wn.update()


