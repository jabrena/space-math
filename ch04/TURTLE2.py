from ce_turtl import *

def koch(a,gen):
    if gen>0:
        for t in [60,-120,60,0]:
            turtle.forward(a/3)
            turtle.left(t)
    else:
        turtle.forward(a)
turtle.penup()
turtle.goto(-100,-50)
turtle.color(255,0,0)
turtle.pendown()
koch(200,1)
turtle.show()