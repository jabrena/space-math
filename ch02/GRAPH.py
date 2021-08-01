import ti_plotlib as plt

# After running the program, press [clear] to clear plot and return to Shell.


def f(x):
    return 3*x**2-.4


def g(x):
    return -f(x)


def plot(res, xmin, xmax):
    # setup plotting area

    plt.window(xmin, xmax, xmin/1.5, xmax/1.5)
    plt.cls()
    gscale = 5
    plt.grid((plt.xmax-plt.xmin)/gscale*(3/4),
             (plt.ymax-plt.ymin)/gscale, "dash")
    plt.pen("thin", "solid")
    plt.color(0, 0, 0)
    plt.axes("on")
    plt.labels("abscisse", " ordonnee", 6, 1)
    plt.pen("medium", "solid")

    # plot f(x) and g(x)
    dX = (plt.xmax - plt.xmin)/res
    x = plt.xmin
    x0 = x
    for i in range(res):
        plt.color(255, 0, 0)
        plt.line(x0, f(x0), x, f(x), "")
        plt.color(0, 0, 255)
        plt.plot(x, g(x), "o")

        x0 = x

        x += dX

    plt.show_plot()


# plot(resolution,xmin,xmax)
plot(30, -1, 1)

# Create a graph with parameters(resolution,xmin,xmax)

# After clearing the first graph, press the [var] key. The plot() function allows you to change the display settings (resolution,xmin,xmax).
