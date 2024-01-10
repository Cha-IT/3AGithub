import matplotlib.pyplot as plt

def f(x):
    """ En helt vanlig python funksjon,
    Men vi kaller den f for den matematiske funksjonen
    """

    a=x**2 
    return a
xverdier=[]
yverdier=[]

for x in range(10):
    xverdier.append(x)
    yverdier.append( f(x) )


plt.plot(xverdier,yverdier) #Plotter grafen
plt.show()                  #Tegner grafen


