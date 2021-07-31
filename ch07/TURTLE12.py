from ce_turtl import *

colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']

turtle.clear()
turtle.penup()
for x in range(360):
    turtle.color(colors[x % 6])
    turtle.width(x / 5 + 1)
    turtle.forward(x)
    turtle.left(20)
turtle.show()