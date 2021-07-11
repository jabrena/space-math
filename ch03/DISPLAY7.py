import ti_plotlib as plt 
from math import *

def f(x,y):
    return cos(x-y)

def g(x, y):
    return sin(x*y)

def plot(res,xmin,xmax):
    plt.window(xmin,xmax,xmin/1.5,xmax/1.5)
    plt.cls()
    gscale=5
    plt.grid((plt.xmax-plt.xmin)/gscale*(3/4),(plt.ymax-plt.ymin)/gscale,"dash")
    plt.pen("thin","solid")
    plt.color(0,0,0)
    plt.axes("on")
    plt.pen("medium","solid")
    
    d = (plt.xmax - plt.xmin)/res
    y = plt.ymin
    y0 = y
    diagonal = sqrt(res**2 + (res//1.5)**2)/2
    for j in range(res//1.5):
        x = plt.xmin
        x0 = x
        for i in range(res):
            if abs(f(x, y) - g(x, y)) < d * 0.9:
                red = sqrt((i-res/2)**2+(j-res//3)**2)/(diagonal)*255    
                green = 255 - (abs(j-res//3)/(res//3))*255  
                blue = 255 - (abs(i-res/2)/(res/2))*255  
                plt.color(red,green,blue)
                plt.line(x0, y0, x, y,"")
            x0 = x
            x += d
        y0 = y
        y += d


    plt.show_plot()

#plot(resolution,xmin,xmax)

plot(100,-10,10)

# Create a graph with parameters(resolution,xmin,xmax)

# After clearing the first graph, press the [var] key. The plot() function allows you to change the display settings (resolution,xmin,xmax).