from ce_turtl import *

turtle.clear()
turtle.pensize(0)

turtle.penup()
turtle.goto(0, -15)
turtle.pendown()

for i in range(100):
    turtle.forward(10+(i/6)*5)
    turtle.left(60)

turtle.show()