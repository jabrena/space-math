#import turtle
from ce_turtl import *

turtle.clear()
turtle.penup()
turtle.goto(-50, -90)
turtle.pendown()
for i in range(6):
    turtle.forward(100)
    turtle.right(300)
turtle.show()
