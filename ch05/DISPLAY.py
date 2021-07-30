import ti_plotlib as plt

plt.cls()
n=0
plt.window(-160, 160, -180, 180)
for i in range(53):
    plt.color(235, 42+n, 52)
    plt.line(-160+i, 180, -160+i, -180, "")
    n = n+4
