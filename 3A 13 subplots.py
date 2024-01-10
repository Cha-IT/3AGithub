import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)

# Graf 1
yverdier = 0.5*xverdier**2 
fig,axs = plt.subplots(2,1)
fig.suptitle("Super overskrift")
print(axs)   
axs[0].plot(xverdier, yverdier)


# Graf 2
yverdier = -0.3*xverdier**3 
axs[1].plot(xverdier, yverdier)

for ax in axs.flat:
    ax.set_title("TEST")
    ax.set(xlabel='x-label', ylabel='y-label')

plt.show()