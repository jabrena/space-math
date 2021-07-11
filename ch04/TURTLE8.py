from ce_turtl import *

def hilbert(n,length):
  lhlb(n,length)

def lhlb(n,length):
  if n<=0:
    return 
  turtle.right(90)
  rhlb(n-1,length)
  turtle.forward(length)
  turtle.left(90)
  lhlb(n-1,length)
  turtle.forward(length)
  lhlb(n-1,length)
  turtle.left(90)
  turtle.forward(length)
  rhlb(n-1,length)
  turtle.right(90)

def rhlb(n,length):
  if n<=0:
    return 
  turtle.left(90)
  lhlb(n-1,length)
  turtle.forward(length)
  turtle.right(90)
  rhlb(n-1,length)
  turtle.forward(length)
  rhlb(n-1,length)
  turtle.right(90)
  turtle.forward(length)
  lhlb(n-1,length)
  turtle.left(90)

def myt08():
  turtle.home()
  turtle.clear()
  turtle.speed(10)
  turtle.penup()
  turtle.goto(-110,110)
  turtle.pendown()
  hilbert(5,7)
  turtle.penup()
  turtle.goto(-150,-100)
  turtle.show()
myt08()