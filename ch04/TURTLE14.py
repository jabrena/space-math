from ce_turtl import *

turtle.clear()
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

for i in range(30):
    turtle.circle(5+i*5)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)

turtle.show()