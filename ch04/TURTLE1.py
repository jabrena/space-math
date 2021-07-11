from ce_turtl import *

turtle.clear()
turtle.penup()
turtle.pensize(1)
turtle.color(0,0,255)
turtle.goto(-50,-50)
turtle.pendown()
for i in range(4):
    turtle.forward(100)
    turtle.left(360/4)
turtle.show()