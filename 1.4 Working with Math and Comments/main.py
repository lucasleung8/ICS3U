#Math calculator using 3 functions from the math library. Created By Lucas L. for ICS3U course, Feb 22 2023

import math

######SQUARE ROOT FUNCTION######
#getting input from user, convert to int
sqrtRequested = int(input('Enter a number to find the squareroot of it: '))

#calculating the squareroot of the chosen number
sqrtAns = math.sqrt(sqrtRequested)

#resulting print statement
print(f'The squareroot of {sqrtRequested} is {sqrtAns}')

######SINE FUNCTION######
#getting integer input from user to know what angle is to be used
sineRequested = int(input('Enter an angle to find the sine of it, in both degrees and radians: '))

#calculates sine of chosen angle in radians.
sineAnsInRadians = math.sin(sineRequested)

#convert angle from degrees to radians and calculate sine
sineRequestedInRadians = math.radians(sineRequested)
sineAnsInDegrees = math.sin(sineRequestedInRadians)

#resulting print statement
print(f'Degrees: The sin of {sineRequested} is {sineAnsInDegrees}')
print(f'Radians: The sin of {sineRequested} is {sineAnsInRadians}')
