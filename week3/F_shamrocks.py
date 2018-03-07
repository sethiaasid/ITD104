#----------------------------------------------------------------------
#  Luck of the Irish
#
#  As another example of code reuse, in this exercise you will develop
#  a Turtle graphics function to draw a shamrock (a three-leaf clover)
#  and use it to populate an Irish field.
#

# Import the turtle graphics functions
from turtle import *
from random import randint

# Set up the "grassy field"
field_size = 600 # pixels
setup(field_size, field_size)
bgcolor("dark green")
title("Luck of the Irish")
color("green")
# Adjust the drawing speed, if necessary
speed('fastest')


#----------
# Step 1
#
# Define a function that draws a single shamrock.  It should have
# two parameters, the x and y coordinates at which to draw the
# image.  The shamrock should consist of three circular leaves and
# a stem.  Choose an appropriate colour, distinct from the background.

### PUT YOUR FUNCTION DEFINITION HERE
def heart(angle):
	pendown()
	begin_fill()
	setheading(angle)
	left(53)
	forward(20)
	left(37)
	circle(6, 180)
	left(180)
	circle(6, 180)
	left(37)
	forward(20)
	end_fill()

def shamrock(x, y, angle):
	penup()

	goto(x, y)
	heart(0 + angle)
	goto(x, y)
	heart(90 + angle)
	goto(x, y)
	heart(270 + angle)
	goto(x, y)
	pendown()
	setheading(270 + angle)
	forward(20)


#----------
# Step 2
#
# Write a main program to display 50 (or so) shamrocks randomly
# positioned on the field.  Use the field size defined above
# to limit the placement of shamrocks.

### PUT YOUR MAIN PROGRAM HERE
shamrock_size = 50
for i in range(shamrock_size):
	shamrock(randint(-field_size/2, field_size/2)
		, randint(-field_size/2, field_size/2), randint(0, 360))


# Exit gracefully
hideturtle()
done()
