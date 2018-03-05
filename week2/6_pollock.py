##  Jackson Pollock's Final Masterpiece
##
##  20th century "artists" such as Jackson Pollock achieved fame
##  by stumbling drunkenly around a canvas on the floor
##  dribbling paint out of tins. (We're not being rude - he openly
##  admitted to being drunk when creating his paintings.) However,
##  today we can achieve the same effect without getting our hands
##  dirty or taking a swig by using Python!
##  
##  Using Turtle graphics develop a program to draw many blobs 
##  (dots) of random colour, size and location on the screen.
##  The blobs should be connected by lines of "paint" of
##  various widths as if paint had been dribbled from one
##  blob to the next.  The "paint" should not go off the edge
##  of the "canvas".  Use the following solution strategy.
##
##    1. Set up the blank canvas of a known size
##    2. Ensure the pen is down
##    3. For each "blob" in a large range:
##       a. Select a random pen colour
##       b. Pick a random pen width
##       c. Go to a random location on the screen
##          (drawing as you go)
##       d. Draw a blob (dot)
##    4. Exit the program gracefully
##
##  Hint: Although you could select colours from a list of
##  names, you can get a wider range of colours, by noting
##  that Turtle's "color" function can accept three numbers
##  as arguments, representing red-green-blue pixel densities.
##  These numbers are floating point values between 0.0 and 1.0.
##  Also note that the "random" module's "uniform" function
##  produces a random floating point number.
##
##  Hint: This exercise is actually very similar to the
##  previous "Starry, Starry Night" one, so you can develop
##  your solution as an extension of that.


# Import the functions required
from turtle import *
from random import uniform, randint


## DEVELOP YOUR PROGRAM HERE
max_blob = 200
max_pen_width = 50
max_dot_diameter = 100

width = 700
height = 700

setup(width, height)
title("Jackson Pollock")
hideturtle()

for i in range(max_blob):
	pencolor(uniform(0, 1), uniform(0, 1), uniform(0, 1))
	pensize(randint(1, max_pen_width))
	goto(randint(-width/2, width/2), randint(-height/2, height/2))
	dot(randint(1, max_dot_diameter))
	
done()

# num_star = 200
# width = 700
# height = 700
# size_star = 20

# setup(width, height)
# title("Starry night")
# bgcolor("black")
# penup()
# hideturtle()
# speed('fastest')
# colormode(255)

# for i in range(num_star):
	# goto(randint(- (width/2), (width/2)), randint(- (height/2), (height/2)))
	# r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
	
	# dot(randint(1, size_star), (r, g, b))

# done()