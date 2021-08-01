
# Solution

import random as r
import math as m

try :
    import ti_plotlib as plt

    ti84_platform = True
except :
    ti84_platform = False

if not ti84_platform :
    raise Exception("This program is only available for TI-84 Plus CE T Python")

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

def screenSetup() :

    plt.cls()
    plt.window(0,1,0,1)
    plt.axes("on")
    plt.grid(1, 1, "dot")
    plt.title("Estimating Pi with Montecarlo")

def showLegend(counter, i, iterations) :

    plt.color(0,0,0)
    plt.text_at(7,  str(m.pi), "left")
    plt.text_at(8,  str(calculatePi(counter, iterations)), "left")
    plt.text_at(9,  str(m.pi - calculatePi(counter, iterations)), "left")
    plt.text_at(10, str(i+1), "left")

def problem (iterations) : 

    screenSetup()    

    radius = 1.0
    counter = 0
    for i in range(0, iterations) :

        point = getPoint()
        if isPointInside(point, radius) :
            counter += 1
            plt.color(28,242,221)
        else :
            plt.color(153, 133, 122)
        plt.plot(point[0], point[1])

        showLegend(counter, i, iterations)

    plt.show_plot()
    
    return calculatePi(counter, iterations)

# Asserts
iterations = int(input("Number of iterations?"))
problem(iterations)

# References
# https://blogs.sas.com/content/iml/2016/03/14/monte-carlo-estimates-of-pi.html
