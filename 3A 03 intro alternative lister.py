import matplotlib.pyplot as plt
import numpy as np
def f(x):
    """ En helt vanlig python funksjon,
    Men vi kaller den f for den matematiske funksjonen
    """
    a=x**2 
    return a

# Med listeutrulling: 
xverdier1=[ x for x in range(11)]
yverdier1=[f(x) for x in xverdier1]

# Med bruk av numpy
xverdier2 = np.linspace(0,10,11) #(start, stopp, Antall_steg)
yverdier2 = f(xverdier2)
# Fordel, kan bruke x-verdiene direkte
# Kan enkelt fordele verdiene, og ha flyttall

print(xverdier1)
print(yverdier1)
print(xverdier2)
print(yverdier2)
# plt.plot(xverdier,yverdier) #Plotter grafen
# plt.show()                  #Tegner grafen


