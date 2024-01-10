import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)
yverdier = xverdier**2

# Skriver ut en oversikt over tilgjengelige stiler
print(plt.style.available)

# Angir at vi vil bruke stilen "bmh"
plt.style.use("Solarize_Light2")

plt.plot(xverdier, yverdier)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0, 20)
plt.ylim(0, 400)

plt.show()