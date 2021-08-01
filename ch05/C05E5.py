from ti_system import disp_wait
import ti_plotlib as plt

xmin, xmax, ymin, ymax = 0, 319, 30, 239

plt.cls()
plt.window(-160, 160, -180, 180)

def draw() :

    n = 0
    for i in range(xmax):

        r = 235
        g = 42 + n
        b = 52

        if g >= 255 :
            n = 0
            g = 0

        plt.color(r, g, b)
        plt.line(-160 + i, 180, -160 + i, -180, "")
        
        n = n + 4

draw()
disp_wait()
