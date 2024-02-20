"""
Name: question_5.py

Description:

Draw shapes.

Author: Rae Harbird

Date: August 2018

Here is a list of colours: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
"""

from turtle import *


# Function to draw a polygon


def draw_n_gon(sides, side_length):
    
    for counter in range(sides):
        fd(side_length)
        lt(360/sides)


# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw triangle
draw_n_gon(3, 50)

# move the turtle along
penup()
fd(75)
pendown()

# change the colour of the pen
pencolor("blue")

draw_n_gon(4, 40)

# move the turtle along
penup()
fd(75)
pendown()

# change the colour of the pen
pencolor("green")

draw_n_gon(5, 50)

# move the turtle along
penup()
fd(125)
pendown()

# change the colour of the pen
pencolor("red")

draw_n_gon(6, 60)

# move the turtle along
penup()
fd(175)
pendown()

# change the colour of the pen
pencolor("pink")

draw_n_gon(8, 80)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()
