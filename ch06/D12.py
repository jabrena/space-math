from ti_system import *
import ti_graphics as scr

tw = 10
s = 'Thank you TI'
xmin, xmax, ymin, ymax = 0, 319, 30, 239
x, y, dx, dy = xmin, ymin, 1, 9

scr.cls()
while x <= xmax - tw * len(s):
  scr.drawString(s, x, y)
  y += dy
  x += dx
  dx += 1

disp_wait()