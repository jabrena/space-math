from ce_turtl import *

turtle.home()
turtle.clear()

for i in range(200):
    #turtle.circle(100, 60-i)
    turtle.circle(60-i)
    turtle.left(i)

turtle.show()
