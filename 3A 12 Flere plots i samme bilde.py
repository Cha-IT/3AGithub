import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)

# Graf 1
yverdier = 0.5*xverdier**2 
plt.title("$0.5*x^2$")

plt.subplot(2, 1, 1)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 2
yverdier = -0.3*xverdier**3 

plt.subplot(2, 1, 2)
plt.plot(xverdier, yverdier)
plt.title("$-0.5*x^3$")
plt.grid()

plt.show()

plt.tight_layout()

