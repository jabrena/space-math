from ce_turtl import *

turtle.clear()
turtle.penup()

for a in range(40, -1, -1):
    turtle.pendown()
    # turtle.stamp()
    turtle.left(a)
    turtle.forward(20)

turtle.show()
