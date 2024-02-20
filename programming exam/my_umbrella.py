#!/usr/bin/env python3
'''
Program name: my_umbrella.py
Student number: 20021899

Draw an umbrella of a given UMBRELLA_RADIUS, with a variable number of "cloth" sections, with all sections being equal size.
'''

from tkinter import Y
import turtle
import random
import math

NUM_SECTIONS = 9
UMBRELLA_RADIUS = 200

def move_to(x_pos: int, y_pos: int):
    """Move turtle to position at x_pos, y_pos.

    Args:
        pos_x: Horizontal position (in pixels) where the turtle is moved to.
        pos_y: Vertical position (in pixels) where the turtle is moved to.        
    """
    turtle.penup()
    turtle.goto(x_pos, y_pos)
    turtle.pendown()

def RGB():
    """ randomly assign RBG color numbers and fill color with R,G,B no.

    Args:
        R, G, B: ramdom assigned numbers
    """

    R = random.random()
    G = random.random()
    B = random.random()

    turtle.fillcolor(R, G, B)

def main():
    # Insert your code here
    # calculate length of each edge
    x = (math.sin(math.radians(20)))*UMBRELLA_RADIUS*2
    
    #start draw
    for n in range(NUM_SECTIONS):
        # set start position
        move_to(0,0)
        turtle.pd()
        # set pencolor
        turtle.pencolor("black")
        # Call the RGB function to get a random color filled
        RGB()
        turtle.begin_fill()
        # Start drawing a triangle 
        turtle.fd(UMBRELLA_RADIUS)
        turtle.lt(110)
        turtle.fd(x)
        turtle.lt(110)
        turtle.fd(UMBRELLA_RADIUS)
        turtle.lt(180)
        turtle.end_fill()  
        turtle.pu()
    pass
    # Do not delete turtle.exitonclick()
    turtle.exitonclick()


if __name__ == "__main__":
    main()