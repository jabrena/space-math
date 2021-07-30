from ce_turtl import *

def fractal(size,depth=0):
  if depth<=0:
    turtle.forward(size)
  else:
    fractal(size/3,depth-1);turtle.left(60)
    fractal(size/3,depth-1);turtle.left(-120)
    fractal(size/3,depth-1);turtle.left(60)
    fractal(size/3,depth-1)

def myt03():
  for j in range(3):
    turtle.home()
    turtle.clear()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-60,-108)
    turtle.pendown()
    for i in "12345":
      fractal(140,j+1)
      turtle.left(360/5)
    turtle.penup()
  turtle.goto(-150,-100)
  turtle.show()
myt03()