import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**2

xverdier = np.linspace(0, 10, 50)
yverdier = f(xverdier)

# plt.plot(xverdier, yverdier,"^:k")
plt.plot(xverdier, 1*yverdier, color="black", linestyle="dashed", marker="^")
plt.plot(xverdier, 2*yverdier, color="black", linestyle="dashed", marker="^",
          linewidth=1, markersize=10,markevery=2, zorder=2, #test
          markeredgecolor="r",markerfacecolor="yellow")

plt.grid()
plt.title("Funksjonen $f(x)=x^2$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0, 10)
plt.ylim(0, 150)

plt.show()