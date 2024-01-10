import matplotlib.pyplot as plt

xverdier = [3, 6, 9]        #Liste med x-verdier
yverdier = [2, 4, 6]        #Liste med y-verdier

plt.plot(xverdier,yverdier) #Lager grafen
plt.savefig("test.jpg", dpi=300, transparent=False) #Lagrer grafen
plt.show()                  #Tegner grafen

