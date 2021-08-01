from ce_turtl import *

turtle.home()
turtle.clear()

for i in range(600):
    if i % 5 == 0:
        turtle.left(3)
    turtle.forward(200)
    turtle.left(360/5)

turtle.show()
