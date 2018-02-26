# Change Calculator
#
# THE PROBLEM
#
# You need to calculate how much change is due when you go shopping.
# You have a $20 note and buy the following:
#   2 cartons of milk @ $2.50
#   5 Mars bars @ $1.20 each
#   1 pkt indigestion tablets @ $3.50
#
# Write an expression to calculate the change you should be given
# from $20, after buying those groceries.  Display the value of the
# change in a message to the screen.

# Assign cost for items and budget
milk = 2.5
mars_bars = 1.2 * 5.0
tablets = 3.5
budget = 20.0

# Calculate the total cost
total = milk + mars_bars + tablets

# Calculate the change after deducting total cost
change = budget - total

print("Your change is: $%.2f" % (change))

# HINTS:
# * You will need to use built-in mathematical operators: *, + and -
# * You may like to introduce variables to accumulate and store values
# * The Python command "print E" will print the value of expression E

