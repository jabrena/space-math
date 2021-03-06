# Leibniz's Formula for Pi
#
# pi/4 = 1-1/3+1/5-1/7+1/9
#

# Solution

from math import *


def problem(iterations):

    pi = 1

    for x in range(0, iterations):

        den = (x * 2 + 3)
        if (x % 2 == 0):
            pi -= (float(1) / float(den))
        else:
            pi += (float(1) / float(den))

    pi *= 4
    return pi

# Asserts


iterations = 10000
print(pi)
print(problem(iterations))
print(pi - problem(iterations))

# Links
# https://javapapers.com/java/java-puzzle-floating-point-precision/
# https://docs.python.org/3/tutorial/floatingpoint.html
# https://www.geeksforgeeks.org/floating-point-error-in-python/
# https://stackoverflow.com/questions/19473770/how-to-avoid-floating-point-errors
