"""
 Name: question_7.py

Description:

Draw spirals.

Author: Rae Harbird

Date: August 2018

Here is a list of colours: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
"""

from turtle import *


# Function to draw a polygon spiral

def draw_n_gon_spiral(sides, side_length, spiral_revolutions):
    for i in range(spiral_revolutions):
        for counter in range(sides):
            fd(side_length)
            lt(360/sides)
            side_length = side_length + 3


# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)
pendown()

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw triangle spiral
draw_n_gon_spiral(3, 3, 5)

# move the turtle along
penup()
setpos(-275, 0)
pendown()

# change the colour of the pen
pencolor("blue")

draw_n_gon_spiral(4, 4, 5)
# move the turtle along
penup()
setpos(-150, 0)
pendown()

# change the colour of the pen
pencolor("green")

draw_n_gon_spiral(5, 5, 5)

# move the turtle along
penup()
setpos(25, 0)
pendown()

# change the colour of the pen
pencolor("red")

draw_n_gon_spiral(6, 6, 5)

# move the turtle along
penup()
setpos(300, 0)
pendown()

# change the colour of the pen
pencolor("pink")

draw_n_gon_spiral(8, 7, 5)


# leave the turtle on the screen until the user clicks in the screen
exitonclick()
