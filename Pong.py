# Simple Pong in python 3 for beginners
# by @Stephen Blaney

#Part 1 : Getting Started

import turtle

wn = turtle.Screen() #screen object
wn.title("Pong by Stephen Blaney")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Main game loop

while True:
    wn.update()


