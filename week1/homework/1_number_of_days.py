# Days calculator
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, representing the number of days in each
# month of a given (non-leap) year.

january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31


# PART 1
#
# Write an expression, or expressions, to calculate the number of days
# in each quarter (three month period) of the year, using the values
# introduced above, and print the result.

first_quarter = january + february + march
second_quarter = april + may + june
third_quarter = july + august + september
last_quarter = october + november + december

print("There are ", first_quarter, " days in first quarter.")
print("There are ", second_quarter, " days in second quarter.")
print("There are ", third_quarter, " days in third quarter.")
print("There are ", last_quarter, " days in last quarter.")



# PART 2
#
# Write an expression, or expressions, to calculate the number of days
# in each half of the calendar year, and print the result.  NB: Your
# solution to Part 2 should use your solution to Part 1.

first_half = first_quarter + second_quarter
second_half = third_quarter + last_quarter

print("There are ", first_half, " days in first half.")
print("There are ", second_half, " days in second half.")

# PART 3
#
# Write an expression, or expressions, to calculate the number of days
# in the year, and print the result  NB: Your solution to Part 3
# should use your solution to Part 2.

print("There are ", first_half + second_half, " days in a year.")


