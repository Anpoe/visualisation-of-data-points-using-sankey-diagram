"""
Name: question_4.py

Description:

Draw shapes.

Author: Rae Harbird

Date: August 2018

Here is a list of colours: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
"""

from turtle import *


# Function to draw a triangle


def draw_triangle(side_length):
    
    for counter in range(3):
        fd(side_length)
        lt(120)


# Function to draw a square

def draw_square(side_length):
    
    for counter in range(4):
        fd(side_length)
        lt(90)


# Function to draw a pentagon


def draw_pentagon(side_length):
    
    for counter in range(5):
        fd(side_length)
        lt(360/5)


# Function to draw a hexagon


def draw_hexagon(side_length):
    
    for counter in range(6):
        fd(side_length)
        lt(360/6)


# Function to draw a octagon


def draw_octagon(side_length):
    
    for counter in range(8):
        fd(side_length)
        lt(360/8)


# place the turtle on the left hand side of your canvas

penup()
setpos(-300, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw triangle
draw_triangle(30)

# move the turtle along
penup()
fd(50)
pendown()

# change the colour of the pen
pencolor("blue")

draw_square(40)

# move the turtle along
penup()
fd(75)
pendown()

# change the colour of the pen
pencolor("green")

draw_pentagon(50)

# move the turtle along
penup()
fd(125)
pendown()

# change the colour of the pen
pencolor("red")

draw_hexagon(60)

# move the turtle along
penup()
fd(175)
pendown()

# change the colour of the pen
pencolor("pink")

draw_octagon(80)


# leave the turtle on the screen until the user clicks in the screen
exitonclick()
