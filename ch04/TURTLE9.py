from ce_turtl import *

def square():
  for i in range(4):
    turtle.forward(65)
    turtle.right(90)

def myt11():
  turtle.home()
  turtle.clear()
  turtle.speed(10)
  for i in range(72):
    square()
    turtle.right(5)
  turtle.penup()
  turtle.goto(-150,-100)
  turtle.show()
myt11()