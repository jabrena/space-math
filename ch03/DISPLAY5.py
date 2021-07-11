from ti_graphics import *
from ti_system import disp_wait

def myDrawString(s, x, y, cf, cb=None):
  if cb:
    setColor(cb)
    fillRect(x, y, 10 * len(s), 15)
  setColor(cf)
  drawString(s, x, y)   

myDrawString("Hallo World", 0, 30, (255, 255, 0), (0, 0, 255))

setColor((255,255,0))
fillRect(200,30,120,15)

setColor((0,0,255))
fillRect(300,30,19,15)

for i in range(200,320,3):
  setPixel(i,40,(255,0,0))

disp_wait()