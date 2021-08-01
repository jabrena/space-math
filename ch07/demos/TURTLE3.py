from ce_turtl import *


def koch(a, gen):
    if gen > 0:
        for t in [60, -120, 60, 0]:
            koch(a/3, gen-1)
            turtle.left(t)
    else:
        turtle.forward(a)


turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.pensize(0)
turtle.color(255, 0, 0)
koch(200, 4)
turtle.show()
