from ce_turtl import *

def myt01():
  l=70
  turtle.home()
  turtle.clear()
  turtle.speed(10)
  turtle.penup()
  turtle.goto(0-l,0+l/2)
  turtle.pendown()
  for i in range(36):
    turtle.forward(140)
    turtle.right(360/3+10)
  turtle.penup()
  turtle.goto(-100,-100)
  turtle.show()
myt01()