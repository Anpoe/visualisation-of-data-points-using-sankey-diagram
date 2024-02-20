"""
Name: question_3.py

Description:

Draw 4 squares.

Author: Rae Harbird

Date: August 2018

Here is a list of colours: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
"""

import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

# Function to draw a square


def draw_square(side_length):
    
    for counter in range(4):
        my_turtle.fd(side_length)
        my_turtle.lt(90)


# place the turtle on the left hand side of your canvas
my_turtle.penup()
my_turtle.setpos(-225, 0)
my_turtle.pendown()

# set the pen width
my_turtle.pensize(2)

# set the pen colour to a green colour
my_turtle.pencolor("DarkOliveGreen4")

# Draw smallest square
draw_square(50)

# Draw next square
# move the turtle along
my_turtle.penup()
my_turtle.fd(75)
my_turtle.pendown()

# change the colour of the pen
my_turtle.pencolor("blue")

draw_square(75)

# move the turtle along
my_turtle.penup()
my_turtle.fd(100)
my_turtle.pendown()

# change the colour of the pen
my_turtle.pencolor("green")

draw_square(100)

# move the turtle along
my_turtle.penup()
my_turtle.fd(125)
my_turtle.pendown()

# change the colour of the pen
my_turtle.pencolor("red")

draw_square(100)
