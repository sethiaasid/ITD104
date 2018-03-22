#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 10274472
#    Student name: TONG XUAN BAO
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/) [1PT8102].
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  FOUR PIECE JIGSAW PUZZLE
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_attempt".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a jigsaw puzzle whose
#  state of completion is determined by data stored in a list which
#  specifies the locations of the pieces.  You are also required to
#  provide a solution to your particular puzzle.  See the instruction
#  sheet accompanying this file for full details.
#
#  This template file must be used and you will submit
#  your final solution as a single file only.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.


##size_of_pieces = 300 # pixels (excluding any protruding "tabs")
size_of_pieces = 300 # pixels (excluding any protruding "tabs")
half_piece_size = size_of_pieces / 2
max_tab_size = 100 # pixels
box_size = size_of_pieces + (max_tab_size * 2)
half_box_size = box_size / 2
left_border = max_tab_size
gap = max_tab_size
top_bottom_border = max_tab_size
canvas_height = (top_bottom_border + size_of_pieces) * 2
canvas_width = (size_of_pieces * 2 + left_border) * 2
template_centres = [[-(size_of_pieces + half_piece_size), -half_piece_size], # bottom left
                    [-half_piece_size, -half_piece_size], # bottom right
                    [-(size_of_pieces + half_piece_size), half_piece_size], # top left
                    [-half_piece_size, half_piece_size]] # top right
box_centre = [gap + (box_size / 2), 0]

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background for the puzzle, i.e., the template for the
# pieces and the box they're kept in.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up and at its standard width and colour.
#


# Draw the box that contains unused puzzle pieces.  (The box is
# larger than the puzzle pieces to allow for tabs sticking out on
# any of their four sides.)
def draw_box():

    # Determine the position of the box's bottom-left corner
    bottom_left = [box_centre[0] - half_box_size,
                   box_centre[1] - half_box_size]

    # Go to the bottom-left corner and get ready to draw
    penup()
    goto(bottom_left)
    width(5)
    color('black')
    pendown()
    
    # Walk around the box's perimeter
    setheading(0) # point east
    for side in [1, 2, 3, 4]:
        forward(box_size)
        left(90)

    # Reset the pen
    width(1)
    penup()
 

# Draw the individual squares of the jigsaw's template
def draw_template(show_template = False):

    # Only draw if the argument is True
    if show_template:

        # Set up the pen
        width(3)
        color('grey')

        # Draw a box for each centre coordinate
        for centre_x, centre_y in template_centres:
            
            # Determine the position of this square's bottom-left corner
            bottom_left = [centre_x - half_piece_size,
                           centre_y - half_piece_size]

            # Go to the bottom-left corner and get ready to draw
            penup()
            goto(bottom_left)
            pendown()
        
            # Walk around the square's perimeter
            setheading(0) # point east
            for side in [1, 2, 3, 4]:
                forward(size_of_pieces)
                left(90)

        # Reset the pen
        width(1)
        color('black')
        penup()


# As a debugging aid, mark the coordinates of the centres of
# the template squares and the box
def mark_coords(show_coords = False):

    # Only mark the coordinates if the argument is True
    if show_coords:

        # Don't draw lines between the coordinates
        penup()

        # Go to each coordinate, draw a dot and print the coordinate
        color('black')
        for x_coord, y_coord in template_centres + [box_centre]:
            goto(x_coord, y_coord)
            dot(4)
            write(str(x_coord) + ', ' + str(y_coord),
                  font = ('Arial', 12, 'normal'))

    # Reset the pen
    width(1)
    penup()
               
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# jigsaw puzzle pieces:
#
# 1. The name of the piece, from 'Piece A' to 'Piece D'
# 2. The place to put the piece, either in the template, denoted
#    'Top left', 'Top right', 'Bottom left' or 'Bottom right', or
#    in the unused pieces box, denoted 'In box'
#
# Each data set does not necessarily mention all pieces.  Also notice
# that several pieces may be in the box at the same time, in which
# case they should just be drawn on top of each other.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Most importantly, you must write your own data set at the end
# to provide the correct solution to your puzzle.
#

# The following data set doesn't require drawing any jigsaw pieces
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

attempt_00 = []

# Each of the following data sets put just one piece in the box.
# You may find them useful when creating your individual pieces.

attempt_01 = [['Piece A', 'In box']]
attempt_02 = [['Piece B', 'In box']]
attempt_03 = [['Piece C', 'In box']]
attempt_04 = [['Piece D', 'In box']]

# Each of the following data sets put just one piece in a
# location in the template.

attempt_05 = [['Piece A', 'Top left']]
attempt_06 = [['Piece B', 'Bottom right']]
attempt_07 = [['Piece C', 'Top right']]
attempt_08 = [['Piece D', 'Bottom left']]
attempt_09 = [['Piece A', 'Bottom left']]
attempt_10 = [['Piece B', 'Top left']]
attempt_11 = [['Piece C', 'Bottom right']]
attempt_12 = [['Piece D', 'Top right']]

# Each of the following data sets put all four pieces in the
# box, but in different orders.

attempt_13 = [['Piece A', 'In box'], ['Piece B', 'In box'],
              ['Piece C', 'In box'], ['Piece D', 'In box']]
attempt_14 = [['Piece D', 'In box'], ['Piece C', 'In box'],
              ['Piece B', 'In box'], ['Piece A', 'In box']]
attempt_15 = [['Piece C', 'In box'], ['Piece D', 'In box'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]

# Each of the following data sets uses between two and four pieces,
# either in the template or in the box

attempt_16 = [['Piece A', 'Top right'], ['Piece B', 'Bottom left']]
attempt_17 = [['Piece D', 'Bottom right'], ['Piece C', 'In box']]
attempt_18 = [['Piece C', 'Bottom right'], ['Piece A', 'Bottom right']]
attempt_19 = [['Piece B', 'In box'], ['Piece D', 'Top left'],
              ['Piece C', 'In box']]
attempt_20 = [['Piece C', 'Top left'], ['Piece D', 'Top right'],
              ['Piece A', 'Bottom left']]
attempt_21 = [['Piece A', 'In box'], ['Piece D', 'Bottom left'],
              ['Piece C', 'Top right']]
attempt_22 = [['Piece A', 'Bottom left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom right'], ['Piece D', 'In box']]
attempt_23 = [['Piece D', 'Bottom right'], ['Piece C', 'In box'],
              ['Piece B', 'Top right'], ['Piece A', 'Top left']]
attempt_24 = [['Piece C', 'Bottom right'], ['Piece D', 'Top left'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]
attempt_25 = [['Piece D', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece C', 'Bottom right'], ['Piece A', 'Top right']]
attempt_26 = [['Piece C', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece A', 'Bottom right'], ['Piece D', 'Top right']]
attempt_27 = [['Piece C', 'Bottom left'], ['Piece D', 'In box'],
              ['Piece A', 'Top left'], ['Piece B', 'Top right']]

# Each of the following data sets is a complete attempt at solving
# the puzzle using all four pieces (so there are no pieces left in the box)

attempt_28 = [['Piece A', 'Bottom left'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Top right']]
attempt_29 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]
attempt_30 = [['Piece A', 'Bottom left'], ['Piece B', 'Top left'],
              ['Piece C', 'Bottom right'], ['Piece D', 'Top right']]
attempt_31 = [['Piece A', 'Bottom right'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left'], ['Piece D', 'Top left']]
attempt_32 = [['Piece D', 'Top right'], ['Piece A', 'Bottom left'],
              ['Piece B', 'Top left'], ['Piece C', 'Bottom right']]
attempt_33 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]

# Here you must provide a list which is the correct solution to
# your puzzle.

# ***** Put the solution to your puzzle in this list
solution = [['Piece A', 'Top left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left'], ['Piece D', 'Bottom right']] 

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_attempt" function.
#

#  Define some variables
tab_size = 30 # Circle with a radius is 30 pixels
gap_size = 20 # 3/4 of circle

# Draw a line from (x1, y1) to (x2, y2)
# *** x1, y1 are coordinates of first point
# *** x2, y2 are coordinates of the second point
def line(x1, y1, x2, y2):
    # Setup the pen
    width(4)

    # Go to position 1 then pendown and goto position 2
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

    # Reset the pen
    width(1)
    penup()

# Draw a tab with a given direction at (x, y)
def draw_tab(x, y, direction):
    # Setup the pen
    width(4)

    # tab_heading stores the turtle direction
	# Only this function can use tab_heading	
    tab_heading = {'east' : 315, 'west' : 135, 'north' : 45, 'south' : 225}

    # Go to the position and draw
    penup()
    goto(x, y)
    pendown()
    setheading(tab_heading[direction])
    circle(tab_size, 270) # 3/4 of circle

    # Reset the pen
    width(1)
    penup()

# Draw a filled area with background color "bg_color"
# *** and border color "border_color" with area
def draw_area(area, bg_color, border_color):
	# Fill background
    # Setup fillcolor
    width(0)
    color(bg_color)
	# Fill the area with given area
    begin_fill()
    for x, y in area: # coordinates of the points in area
        goto(x, y)
    end_fill()

	# Draw border
    width(2)
    color(border_color)
    goto(area[0][0], area[0][1]) # Go to first point
    pendown()
    for x, y in area:
        goto(x, y)

	# Reset the pen
    color('black')
    width(1)
    penup()


# Draw piece A at the position (x, y)
def piece_a(x, y):
    top_coor = y + half_piece_size # Highest y in the piece
    bottom_coor = y - half_piece_size # Lowest y in the piece
    left_coor = x - half_piece_size # Highest x in the piece
    right_coor = x + half_piece_size # Lowest x in the piece

    # This variable stores areas of the picture in the piece
    # *** each area is a colection of points
    areas = [
            # The tail of pikachu
            [[-11, -198], [9, -129], [-85, -132], [-134, -25], [-67, -31], 
    		[-1, -42], [51, -54], [79, -62], [71, -91], [57, -130], [49, -149],
    		[24, -150], [29, -158], [31, -170], [25, -186], [12, -197], 
    		[-1, -201], [-11, -198]],
        	# The ear
        	[[97, -6], [79, -4], [65, -2], [53, 2], [33, 7], [9, 18], [-9, 29],
        	[-21, 38], [-33, 50], [-11, 54], [15, 53], [47, 50], [70, 46], 
        	[95, 39], [124, 29], [113, 25], [105, 18], [99, 8], [97, -1], 
        	[97, -6]],
        	# Black part in the ear
        	[[33, 9], [-3, 26], [-21, 39], [-32, 52], [-13, 55], [3, 55], 
        	[15, 54], [16, 39], [21, 26], [33, 9]],
        	# Part of the face
        	[[105, -20], [99, -46], [94, -82], [93, -106], [102, -126], 
        	[105, -133], [102, -147], [149, -147], [149, -23], [141, -27], 
        	[123, -30], [117, -27], [109, -22], [105, -20]],
        	# Red piece in the face 
        	[[150, -43], [141, -39], [130, -43], [126, -50], [122, -62], 
        	[128, -73], [137, -76], [148, -72], [150, -43]],
        	# Black part of the left eye
        	[[147, -46], [143, -46], [139, -48], [138, -53], [138, -58], 
        	[141, -62], [146, -61], [147, -46]],
        	# White part of the left eye
        	[[128, -130], [132, -117], [133, -106], [131, -100], [129, -94], 
        	[126, -88], [122, -84], [117, -78], [111, -75], [105, -74], 
        	[98, -78], [93, -86], [93, -107], [101, -126], [109, -129], 
        	[117, -130], [128, -130]]]

    # Background colors and border colors of areas
    col = [['yellow', 'black'], ['yellow', 'black'], ['black', 'black'], 
    ['yellow', 'black'], ['black', 'black'], ['white', 'white'], 
    ['red', 'black']]

    # Redefine areas
    # (x, y) is the origin of the area
    # if we want to print at the right position
    # we need to add every coordinate with x and y
    for area_index in range(len(areas)):
	    for point_index in range(len(areas[area_index])):
	    	areas[area_index][point_index] = [areas[area_index][point_index][0] \
            + x, areas[area_index][point_index][1] + y]

    # Set up fillcolor
    fillcolor('white')

    # Draw and fill half piece with a tab at the bottom
    goto(left_coor, top_coor) # Begin at the left top corner
    begin_fill()
    line(left_coor, top_coor, left_coor, bottom_coor)
    line(left_coor, bottom_coor, x - gap_size, bottom_coor)
    draw_tab(x - gap_size, bottom_coor, 'south')
    line(pos()[0], pos()[1], right_coor, bottom_coor)
    end_fill()

    # Draw and fill half piece with a blank at the right
    goto(left_coor, top_coor) # Begin at the left top corner
    begin_fill()
    line(left_coor, top_coor, right_coor, top_coor)
    line(right_coor, top_coor, right_coor, y + gap_size)
    draw_tab(right_coor, y + gap_size, 'west')
    line(pos()[0], pos()[1], right_coor, bottom_coor)
    end_fill()

    # Draw areas
    for area_index in range(len(areas)):
    	draw_area(areas[area_index], col[area_index][0], col[area_index][1])


# Draw piece B at the position (x,y)
def piece_b(x, y):
    top_coor = y + half_piece_size # Highest y in the piece
    bottom_coor = y - half_piece_size # Lowest y in the piece
    left_coor = x - half_piece_size # Highest x in the piece
    right_coor = x + half_piece_size # Lowest x in the piece

    # This variable stores areas of the picture in the piece
    # *** each area is a colection of points
    areas = [
            # The whole area of pikachu
            [[-151, 21], [-149, 30], [-137, 33], [-123, 36], [-111, 36], 
    		[-96, 38], [-85, 36], [-72, 34], [-59, 32], [-47, 26], [-39, 23], 
    		[-20, 42], [-1, 59], [18, 74], [41, 87], [62, 97], [83, 104], 
    		[112, 110], [105, 90], [94, 78], [81, 66], [58, 45], [38, 29], 
    		[20, 17], [-11, -6], [-4, -34], [1, -66], [4, -90], [3, -106], 
    		[-1, -117], [-6, -130], [-5, -151], [2, -198], [-7, -200], 
    		[-15, -195], [-22, -189], [-25, -185], [-28, -177], [-29, -169], 
    		[-27, -163], [-25, -155], [-21, -150], [-151, -149], [-151, -22], 
    		[-159, -27], [-179, -30], [-191, -23], [-195, -19], [-191, -8], 
    		[-199, -5], [-201, 5], [-199, 13], [-192, 22], [-181, 28], 
    		[-171, 30], [-161, 27], [-151, 21]],
    		# The red piece on the face
    		[[4, -102], [4, -89], [-1, -80], [-5, -76], [-15, -74], [-26, -82],
    		[-33, -94], [-35, -105], [-35, -114], [-34, -122], [-29, -129], 
    		[-23, -131], [-19, -131], [-13, -127], [-7, -123], [-2, -117], 
    		[3, -110], [3, -99], [4, -102]],
    		# The black piece on the ear
    		[[57, 45], [67, 69], [69, 78], [69, 84], [66, 91], [59, 96], 
    		[80, 103], [96, 108], [112, 110], [105, 93], [93, 78], [81, 66], 
    		[57, 43], [57, 45]],
    		# Small black part of the left eye
    		[[-147, -45], [-145, -50], [-143, -57], [-144, -63], [-150, -70], 
    		[-150, -44], [-147, -45]],
    		# Black part of the right eye
    		[[-29, -50], [-31, -47], [-34, -44], [-38, -42], [-43, -39], 
    		[-50, -42], [-56, -46], [-59, -51], [-59, -61], [-58, -68], 
    		[-52, -73], [-45, -75], [-39, -74], [-33, -72], [-29, -66], 
    		[-28, -62], [-30, -52], [-29, -50]],
    		# White part of the right eye
    		[[-45, -62], [-43, -59], [-41, -56], [-41, -55], [-42, -51], 
    		[-42, -50], [-45, -48], [-47, -46], [-49, -46], [-51, -47], 
    		[-53, -47], [-53, -49], [-55, -50], [-55, -53], [-55, -55], 
    		[-55, -57], [-52, -59], [-48, -62], [-47, -61], [-45, -62]],
    		# The mouth
    		[[-135, -102], [-132, -106], [-128, -108], [-124, -110], 
			[-119, -108], [-102, -103], [-83, -109], [-78, -109], [-75, -108],
			[-69, -101], [-75, -108], [-78, -109], [-83, -109], [-102, -103], 
			[-119, -108], [-124, -110], [-128, -108], [-132, -106], 
			[-135, -102]],
			# The nose
			[[-98, -83], [-100, -86], [-106, -82], [-98, -83]],
			# Small draw of the right hand
			[[-2, -185], [-4, -199], [-2, -185]]]

	# Background colors and border colors of areas
    col = [['yellow', 'black'], ['red', 'black'], ['black', 'black'], 
    ['black', 'black'], ['black', 'black'], ['white', 'white'], 
    ['black', 'black'], ['black', 'black'], ['black', 'black']]

    # Redefine areas
    # (x, y) is the origin of the area
    # if we want to print at the right position
    # we need to add every coordinate with x and y
    for area_index in range(len(areas)):
        for point_index in range(len(areas[area_index])):
            areas[area_index][point_index] = [areas[area_index][point_index][0] \
            + x, areas[area_index][point_index][1] + y]

    # Set up fillcolor
    fillcolor('white')

    # Draw and fill whole piece
    goto(left_coor, top_coor) # Begin at the left top corner
    begin_fill()
    line(left_coor, top_coor, left_coor, y + gap_size)
    draw_tab(left_coor, y + gap_size, 'west')
    line(pos()[0], pos()[1], left_coor, bottom_coor)
    line(left_coor, bottom_coor, x - gap_size, bottom_coor)
    draw_tab(x - gap_size, bottom_coor, 'south')
    line(pos()[0], pos()[1], right_coor, bottom_coor)
    line(right_coor, bottom_coor, right_coor, top_coor)
    line(right_coor, top_coor, left_coor, top_coor) 
    end_fill()

    # Draw areas
    for area_index in range(len(areas)):
        draw_area(areas[area_index], col[area_index][0], col[area_index][1])

    
# Draw piece C at the position (x,y)
def piece_c(x, y):
    top_coor = y + half_piece_size # Highest y in the piece
    bottom_coor = y - half_piece_size # Lowest y in the piece
    left_coor = x - half_piece_size # Highest x in the piece
    right_coor = x + half_piece_size # Lowest x in the piece

    # This variable stores areas of the picture in the piece
    # *** each area is a colection of points
    areas = [
            # Whole piece of the pikachu
            [[-12, 103], [-15, 86], [25, 90], [58, 94], [47, 45], [88, 46], 
		    [84, 31], [81, 14], [79, -6], [80, -22], [83, -38], [89, -53], 
		    [99, -69], [110, -74], [126, -76], [139, -76], [149, -73], 
		    [150, -21], [155, -23], [161, -26], [169, -28], [175, -26], 
		    [182, -25], [187, -21], [193, -17], [197, -13], [199, -7], 
		    [201, -5], [201, 8], [197, 16], [191, 24], [181,30], [167, 32], 
		    [161, 30], [151, 23], [149, 152], [103, 151], [100, 134], [99,118],
		    [97, 95], [96, 77], [93, 69], [81, 70], [94, 126], [43, 134], 
		    [49, 150], [24, 150], [29, 142], [31, 130], [30, 122], [26, 114], 
		    [17, 105], [9, 101], [-5, 100], [-12, 103]],
		    # Left leg
		    [[112, -74], [107, -82], [104, -86], [104, -94], [110, -94], 
		    [111, -97], [118, -93], [123, -95], [143, -82], [144, -75], 
		    [136, -77], [128, -77], [124, -77], [117, -75], [112, -74]],
		    # The brown part of the beginning of the tail
		    [[88, 48], [94, 67], [81, 70], [85, 84], [83, 95], [77, 86], 
		    [75, 93], [69, 83], [67, 95], [57, 81], [47, 44], [88, 47]],
		    # Part of the left hand
		    [[98, 110], [105, 71], [124, 43], [149, 23], [156, 22], [160, 24],
		    [166, 26], [174, 31], [166, 26], [160, 24], [156, 22], [149, 23], 
		    [124, 43], [105, 71], [98, 110]],
		    # Part of the left hand
		    [[142, 129], [149, 117], [142, 129]]]

    # Background colors and border colors of areas
    col = [['yellow', 'black'], ['gold', 'black'], ['SaddleBrown', 'black'], 
    ['black', 'black'], ['black', 'black']]

    # Redefine areas
    # (x, y) is the origin of the area
    # if we want to print at the right position
    # we need to add every coordinate with x and y
    for area_index in range(len(areas)):
        for point_index in range(len(areas[area_index])):
            areas[area_index][point_index] = [areas[area_index][point_index][0] \
            + x, areas[area_index][point_index][1] + y]

    # Set up fillcolor
    fillcolor('white')

    # Draw and fill half piece with a blank on top
    goto(left_coor, bottom_coor) # Begin at the left bottom corner
    begin_fill()
    line(left_coor, bottom_coor, left_coor, top_coor)
    line(left_coor, top_coor, x - gap_size, top_coor)
    draw_tab(x - gap_size, top_coor, 'south')
    line(pos()[0], pos()[1], right_coor, top_coor)
    end_fill()

    # Draw and fill half piece with a tab at the left
    goto(left_coor, bottom_coor) # Begin at the left bottom corner
    begin_fill()
    line(left_coor, bottom_coor, right_coor, bottom_coor)
    line(right_coor, bottom_coor, right_coor, y - gap_size)
    draw_tab(right_coor, y - gap_size, 'east')
    line(pos()[0], pos()[1], right_coor, top_coor)
    end_fill()

    # Draw areas
    for area_index in range(len(areas)):
        draw_area(areas[area_index], col[area_index][0], col[area_index][1])


# Draw piece D at the position (x,y)
def piece_d(x, y):
    top_coor = y + half_piece_size # Highest y in the piece
    bottom_coor = y - half_piece_size # Lowest y in the piece
    left_coor = x - half_piece_size # Highest x in the piece
    right_coor = x + half_piece_size # Lowest x in the piece

    # This variable stores areas of the picture in the piece
    # *** each area is a colection of points
    areas = [
            # The whole piece of pikachu
            [[-150, 149], [-151, 24], [-143, 30], [-132, 31], [-122, 31], 
    		[-111, 25], [-103, 16], [-100, 7], [-100, -6], [-103, -13], 
    		[-109, -19], [-119, -26], [-126, -28], [-134, -29], [-139, -27], 
    		[-146, -22], [-151, -22], [-151, -74], [-139, -68], [-132, -65], 
    		[-125, -62], [-118, -62], [-103, -63], [-91, -63], [-80, -63], 
    		[-75, -66], [-68, -68], [-59, -74], [-48, -77], [-39, -78], 
    		[-31, -78], [-22, -77], [-11, -73], [-2, -66], [4, -59], [9, -52], 
    		[12, -44], [14, -37], [16, -28], [17, -14], [17, -1], [9, 40], 
    		[4, 75], [1, 98], [-4, 98], [-14, 102], [-21, 108], [-26, 114], 
    		[-27, 121], [-28, 127], [-27, 134], [-26, 141], [-23, 145], 
    		[-19, 150], [-150, 149]],
    		# The right leg
    		[[-54, -75], [-55, -82], [-42, -90], [-26, -95], [-19, -94], 
    		[-16, -94], [-14, -89], [-19, -75], [-26, -77], [-34, -78], 
    		[-42, -78], [-54, -75]],
    		# Part of the left hand
    		[[-149, 114], [-135, 90], [-127, 70], [-121, 45], [-124, 39], 
    		[-124, 34], [-124, 39], [-121, 45], [-127, 70], [-135, 90], 
    		[-149, 114]],
    		# The right hand
    		[[-44, 130], [-59, 105], [-68, 89], [-77, 67], [-83, 46], 
    		[-80, 40], [-83, 34], [-76, 26], [-70, 26], [-66, 22], [-64, 22], 
    		[-59, 20], [-52, 27], [-38, 33], [-31, 38], [-24, 45], [-19, 51], 
    		[-16, 57], [-12, 66], [-7, 80], [-6, 90], [-5, 99], [-6, 90], 
			[-7, 80], [-12, 66], [-16, 57], [-19, 51], [-24, 45], [-31, 38], 
			[-38, 33], [-52, 27], [-59, 20], [-64, 22], [-66, 22], [-70, 26], 
			[-76, 26], [-83, 34], [-80, 40], [-83, 46], [-77, 67], [-68, 89], 
			[-59, 105], [-44, 130], ]]

    # Background colors and border colors of areas
    col = [['yellow', 'black'], ['gold', 'black'], ['black', 'black'], 
    ['black', 'black']]

    # Redefine areas
    # (x, y) is the origin of the area
    # if we want to print at the right position
    # we need to add every coordinate with x and y
    for area_index in range(len(areas)):
        for point_index in range(len(areas[area_index])):
            areas[area_index][point_index] = [areas[area_index][point_index][0] \
            + x, areas[area_index][point_index][1] + y]

    # Set up fillcolor
    fillcolor('white')

    # Draw and fill half piece with a blank on top
    goto(right_coor, bottom_coor) # Begin at the right bottom corner
    begin_fill()
    line(right_coor, bottom_coor, left_coor, bottom_coor)
    line(left_coor, bottom_coor, left_coor, y - gap_size)
    draw_tab(left_coor, y - gap_size, 'east')
    line(pos()[0], pos()[1], left_coor, top_coor)
    end_fill()

    # Draw and fill half piece with a blank at the left
    goto(left_coor, top_coor) # Begin at the left top corner
    begin_fill()
    line(left_coor, top_coor, x - gap_size, top_coor)
    draw_tab(x - gap_size, top_coor, 'south')
    line(pos()[0], pos()[1], right_coor, top_coor)
    line(right_coor, top_coor, right_coor, bottom_coor)
    end_fill()
    
    # Draw areas
    for area_index in range(len(areas)):
        draw_area(areas[area_index], col[area_index][0], col[area_index][1])


# Draw the jigsaw pieces as per the provided data set
def draw_attempt(attempt):
    # For every piece in attempt
    for pie in attempt:
        # Get the coordinate of the piece
    	if pie[1] == 'Bottom left':
    		x = template_centres[0][0]
    		y = template_centres[0][1]
    	elif pie[1] == 'Bottom right':
    		x = template_centres[1][0]
    		y = template_centres[1][1]
    	elif pie[1] == 'Top left':
    		x = template_centres[2][0]
    		y = template_centres[2][1]
    	elif pie[1] == 'Top right':
    		x = template_centres[3][0]
    		y = template_centres[3][1]
    	else:
    		x = box_centre[0]
    		y = box_centre[1]

        # Get what piece must be printed
    	if pie[0] == 'Piece A':
    		piece_a(x, y)
    	elif pie[0] == 'Piece B':
    		piece_b(x, y)
    	elif pie[0] == 'Piece C':
    		piece_c(x, y)
    	else:
    		piece_d(x, y)

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing canvas
setup(canvas_width, canvas_height)

# Give the canvas a neutral background colour
# ***** You can change the background colour if necessary to ensure
# ***** good contrast with your puzzle pieces
bgcolor('light grey')


# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by solving your puzzle
title('Four Piece Jigsaw Puzzle - Describe your picture here')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Draw the box that holds unused jigsaw puzzle pieces
draw_box()

# Draw the template that holds the jigsaw pieces
# ***** If you don't want to display the template change the
# ***** argument below to False
draw_template(True)

# Mark the centres of the places where jigsaw puzzle pieces must
# be drawn
# ***** If you don't want to display the coordinates change the
# ***** argument below to False
# mark_coords(True)

# Call the student's function to display the attempted solution
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_attempt(attempt_33)

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#
