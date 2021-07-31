
# Solution

import random as r
import math as m

def getPoint() :
    x = r.random() ** 2
    y = r.random() ** 2
    
    return (x , y)

def isPointInside(point, radius) :

    if m.sqrt(point[0] + point[1]) < radius :
        return True

    return False

def calculatePi(inside, total) :

    # inside / total = pi / 4
    return (float(inside) / total) * 4

def problem (iterations) : 

    counter = 0
    for i in range(0, iterations) :

        point = getPoint()
        if isPointInside(point, 1.0) :
            counter += 1

    return calculatePi(counter, iterations)

# Asserts
iterations = 10000000
print(m.pi)
print(problem(iterations))
print(m.pi - problem(iterations))