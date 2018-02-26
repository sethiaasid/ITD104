# Temperature conversion
#
# THE PROBLEM
#
# Assume the following value has already been entered into the
# Python interpreter, denoting a temperature in degrees Fahrenheit

fahrenheit = 98.6 # degrees

# Write a Python expression to calculate the temperature in Celsius
# and print the result in a message to the screen.
#
# HINT: Given a temperature F in degrees Fahrenheit the equivalent
# temperature C in degrees Celsius is (F - 32) * (5 / 9).

celsius = (fahrenheit - 32) * (5 / 9)
print("%.2f Fahrenheit degrees in Celsius is: %.2f degrees." % (fahrenheit, celsius))


