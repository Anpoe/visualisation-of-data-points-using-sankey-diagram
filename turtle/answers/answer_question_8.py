"""
Name: question_8.py

Description:

Draw stars.

Author: Rae Harbird

Date: August 2018

Here is a list of colours: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
"""

from turtle import *


def draw_reg_star(points, side_length):
    for counter in range(points):
        fd(side_length)
        lt(180+(360/points))
        
       
def draw_2x_ang_star(points, side_length):
    for counter in range(points):
        fd(side_length)
        lt(180-(360/points)*2)
        
        
def draw_half_ang_star(points, side_length):
    for counter in range(points):
        fd(side_length)
        lt(180+(360/points)/2)


speed(1)

# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)
pendown()

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw triangle spiral
draw_reg_star(8, 70)

# move the turtle along
penup()
setpos(-200, -30)
pendown()

# change the colour of the pen
pencolor("blue")

draw_2x_ang_star(10, 70)
# move the turtle along
penup()
setpos(-100, 0)
pendown()

# change the colour of the pen
pencolor("green")

draw_reg_star(12, 70)

# move the turtle along
penup()
setpos(0, 0)
pendown()

# change the colour of the pen
pencolor("red")

draw_half_ang_star(15, 70)

# move the turtle along
penup()
setpos(100, -15)
pendown()

# change the colour of the pen
pencolor("pink")

draw_2x_ang_star(18, 70)


# leave the turtle on the screen until the user clicks in the screen
exitonclick()
