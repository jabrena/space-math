# Example to draw points

from ti_system import disp_wait
import ti_graphics as gra

RED_COLOR = (255, 0, 0)
xmin, xmax, ymin, ymax = 0, 319, 30, 239


def drawPoints():

    gra.cls()
    for i in range(xmin, xmax, 3):
        x = i
        y = 100
        gra.setPixel(i, 100, RED_COLOR)


drawPoints()
disp_wait()
