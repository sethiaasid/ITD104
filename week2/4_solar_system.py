#---------------------------------------------------------------------
#
# Solar system
#
# Space is big. Really big. For we mere mortals it's often hard to
# visualise the immensity of the objects in the heavens.  In this
# exercise we'll try to get an understanding of the relative sizes
# of some of the planets in our solar system, by drawing dots
# representing them all to the same scale.
#
# Below are two lists containing data about some planets in our
# solar system.  Your task is to draw a dot of the suggested colour
# and diameter for each of the planets using Turtle's
# "dot" method.  In between drawing each dot you should move
# the cursor to a different location on the screen so that the
# dots are not all on top of one another.
#
# Optionally, you can also choose to write the planet's name next
# to it, using Turtle's "write" method.  You can change the colour
# of the text displayed using Turtle's "color" method.  To change
# the font size, e.g., to 12, call the "write" method with the
# argument "font=('size=12')".
#
# Importantly, you should not "hardwire" the colours and diameters
# in your code.  You should instead refer to the appropriate list
# element by its index, so that your program can draw different
# planets simply by changing the data in the lists.

from turtle import *

# Lists of data your code should refer to
name = ['Mars', 'Earth', 'Neptune', 'Venus', 'Jupiter']
diameter = [13.6, 25.6, 97.2, 24.2, 285.6] # each pixel represents 500km
colour = ['red', 'light blue', 'light grey', 'yellow', 'tan']

left = -450

# Create a canvas representing the vast emptiness of space
setup()
title('Some planets in our solar system')
bgcolor('black')


##### Put your code for drawing the planets here
# draw from left to right
summ = 0
distance = 160
dis_name = 50

for i in range(len(name)):
	up()
	goto(left+summ, 0)
	dot(diameter[i], colour[i])
	pencolor(colour[i])
	down()
	up()
	goto(pos()[0], pos()[1]+dis_name)
	write(name[i], font=('size=12'))


# Exit gracefully
hideturtle()
done()

