##Simple pythagorean theoroum calculator. Practice for using def and return.

import math

#function used to calculate pythagorean theoroum
def pythag(b, c):
  return math.sqrt(b**2 + c**2)

#ask for the 2 known side lengths of right triangle
b = int(input('First side length of your right triangle: '))
c = int(input('Second side length of your right triangle: '))

#gives the answer
print('The third side length is: ' + str(pythag(b, c)))
