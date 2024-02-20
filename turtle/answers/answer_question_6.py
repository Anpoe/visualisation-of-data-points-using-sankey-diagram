"""
Name: question_6.py

Description:

Draw rotated shapes.

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

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw triangle
for count in range(10):
    draw_n_gon(3, 25)
    lt(36)

# move the turtle along
penup()
fd(75)
pendown()

# change the colour of the pen
pencolor("blue")

for count in range(10):
    draw_n_gon(4, 30)
    lt(36)

# move the turtle along
penup()
fd(125)
pendown()

# change the colour of the pen
pencolor("green")

for count in range(10):
    draw_n_gon(5, 35)
    lt(36)

# move the turtle along
penup()
fd(150)
pendown()

# change the colour of the pen
pencolor("red")

for count in range(10):
    draw_n_gon(6, 40)
    lt(36)

# move the turtle along
penup()
fd(225)
pendown()

# change the colour of the pen
pencolor("pink")

for count in range(10):
    draw_n_gon(8, 45)
    lt(36)


# leave the turtle on the screen until the user clicks in the screen
exitonclick()
