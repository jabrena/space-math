from ce_turtl import *

def draw(l):
  if (l<10):
    return 
  else:
    turtle.forward(l)
    turtle.left(30)
    draw(3*l/4)
    turtle.right(60)
    draw(3*l/4)
    turtle.left(30)
    turtle.backward(l)

def myt04():
  turtle.home()
  turtle.clear()
  turtle.speed(10)
  turtle.penup()
  turtle.goto(0,-105)
  turtle.left(90)
  turtle.pendown()
  draw(65)
  turtle.penup()
  turtle.goto(-150,-100)
  turtle.show()
myt04()