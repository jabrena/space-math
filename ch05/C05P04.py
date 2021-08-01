
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

    radius = 1.0
    counter = 0
    pointList = list()
    for i in range(0, iterations) :

        point = getPoint()
        pointList.append(point)
        if isPointInside(point, radius) :
            counter += 1
    
    numericalResult = calculatePi(counter, iterations)

    return numericalResult

# Asserts
print(getPoint())
iterations = 10000000
print(m.pi)
print(problem(iterations))
print(m.pi - problem(iterations))