#import turtle
from ce_turtl import *

turtle.clear()
turtle.penup()
turtle.goto(-30, 0)
turtle.pendown()

num_of_sides = 5
length_of_side = 50
each_angle = 720.0 / num_of_sides

for i in range(num_of_sides):
    turtle.forward(length_of_side)
    turtle.right(each_angle)

#turtle.done()
turtle.show()