from ce_turtl import *

turtle.clear()
turtle.pensize(0)

turtle.penup()
turtle.goto(0, -30)
turtle.pendown()

for i in range(40):
    turtle.forward(10+i*5)
    turtle.left(120)

turtle.show()