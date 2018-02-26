# Three non-overlapping circles
#
# As a simple exercise in using the Turtle package you are
# required to draw three circles on the screen.  Each circle
# must be of a different size and colour.  Most importantly,
# the circles must not touch or overlap at any point, nor
# can one circle appear inside another.
#
# NB: We want unfilled circles, so you can't use Turtle's
# "dot" function for this purpose.  Also, you must ensure that
# lines are not drawn between or connecting the circles.
#
# The basic strategy for drawing each circle is to lift
# up the pen, move to a suitable location on the screen,
# choose a colour, put the pen down and walk in a circle.
# Having done this once you can copy your code (with minor
# changes) three times.
#
# Observation: Turtle's "circle" function does NOT draw a
# circle centred at the current location.  Instead it causes
# the turtle to walk in a circle, ending up back where
# it started.

from turtle import *

setup()
title('Three non-overlapping circles')

## PUT YOUR CODE HERE
pensize(10)
circle(100)

# move to (-200, -300)
up()
goto(-200,-300)
down()
pencolor("blue")
pensize(20)
circle(150)

# move to (200, -400)
up()
goto(200, -390)
down()
pencolor("red")
pensize(5)
circle(200)


hideturtle()
done()
