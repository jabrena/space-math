# I don´t see any result with this example

from ti_system import *
from ti_graphics import *

def rectf(x, y, w, h, c=(0, 0, 0)):
  for i in range(h):
    for k in range(w):
      setPixel(x+k, y+i, c)

rectf(0,0,5,5)

disp_wait()