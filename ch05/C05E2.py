from ti_system import disp_wait
import ti_graphics as gra

TEXT = "Hello World"
RED_COLOR = (255,0,0)
xmin, xmax, ymin, ymax = 0, 319, 30, 239

def drawText() :

  counter = ymin
  gra.cls()
  for i in range(1, 13):
    x = 0
    y = counter
    gra.setColor(RED_COLOR)
    gra.drawString(TEXT, x, y)
    counter += 15

drawText()

disp_wait()