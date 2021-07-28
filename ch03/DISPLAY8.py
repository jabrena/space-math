import ti_system as system
import ti_plotlib as plt

I = system.recall_list("1")
U = system.recall_list("2")

plt.cls()
plt.auto_window(I, U)
plt.title("Demo")

plt.pen("thin", "solid")
plt.axes("on")

plt.color (0, 0, 255)
plt.labels("I" ,"U" ,11 , 2)
plt.scatter(I, U, "x")

plt.color (255, 0, 0)
plt.pen("thin", "dash")
plt.lin_reg(I, U, "center", 2)
plt.show_plot()