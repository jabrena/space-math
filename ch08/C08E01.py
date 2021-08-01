import ti_system as system
import ti_plotlib as plt

# Load data
DATA1 = system.recall_list("1")
DATA2 = system.recall_list("2")


def setup():

    plt.cls()
    plt.auto_window(DATA1, DATA2)
    plt.title("Data Analysis")
    plt.pen("thin", "solid")
    plt.axes("on")


def showScatter():

    plt.color(0, 0, 255)
    plt.labels("I", "U", 11, 2)
    plt.scatter(DATA1, DATA2, "x")


def showLinearRegression():

    plt.color(255, 0, 0)
    plt.pen("thin", "dash")
    plt.lin_reg(DATA1, DATA2, "center", 2)


def analysis():
    setup()
    showScatter()
    showLinearRegression()


analysis()
plt.show_plot()
