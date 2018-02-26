#---------------------------------------------------------------------
#
# Some exercises involving sequences of values
#
# As we've seen, computer programs can manipulate text and ordered
# collections of values as well as numbers.  (Although, in reality,
# all values manipulated by a computer are really represented by
# zeros and ones!)
#
# Below are a collection of small exercises involving values of
# "string" and "list" type, designed to give you some practice with
# expressions that involve more than just numbers.
#

# Exercise: Draw a square
#
# Defined below are three string-valued variables.  Use these
# variables and Python's "print" and assignment statements to
# display a square with four asterisks on each side and blanks
# in the middle.  (There's more than one way to do this so
# try to find the shortest or most elegant way.)

one_star = '*'
two_stars = '**'
two_blanks = '  '

# Your solution goes here

# Magic!
square = one_star*4+('\n'+one_star+two_blanks+one_star)*2+('\n'+one_star*4)

print(square)


# Exercise: Extract letters by position
#
# Below is a string-valued variable containing the alphabetic
# letters found on the top row of a QWERTY keyboard.  Use it
# to print the word 'PRETTY' by referencing the letters via
# their position.  Recall that we count from zero, so the letter
# 'E' is at position 2 in variable 'letters'.  Try to write
# the shortest expression that does this.

letters = 'QWERTYUIOP' # the top row of letters on a keyboard

# Your solution goes here
index = [9,3,2,4,4,5]
word = ''.join([letters[i] for i in index])

print(word)


# Exercise: Where's Ringo?
#
# When the Beatles visited Australia in 1964 Ringo Starr was in
# hospital with tonsillitis, so he was replaced by drummer Jimmie
# Nicol at the start of the tour, as shown by the variable 'fab_four'
# below.  However, by the time the tour reached Melbourne Ringo
# was back on his feet and rejoined the group, replacing Jimmie.
# Write code to replace Jimmie with Ringo and then print the
# resulting band line up.

fab_four = ['John', 'Paul', 'George', 'Jimmie']

# Your solution goes here

fab_four[fab_four.index('Jimmie')] = 'Ringo'

print("The band line up:", fab_four) 


# Exercise: Counting down and up
#
# The built-in 'range' function can be used to generate lists of
# numbers by providing the first value (inclusive), the final value
# (exclusive) and, optionally, a "step size" for going from the
# first value to the last.  Below are two variables denoting a
# first and last value.  Use them and the 'range' function to print
# a list containing the numbers from the first value up to the
# last (including both) and then from the last value down to the
# first (including both).

first = 5
last = 22

# Your solution goes here

list1 = [i for i in range(first, last+1)]

print(list1)

list2 = [i for i in range(last, first-1, -1)]

print(list2)