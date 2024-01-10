import matplotlib.pyplot as plt

hoyder = [180.0, 189.2, 180.5, 174.9, 180.1, 176.6, 181.3, 195.9, 173.4, 184.1, 169.6, 175.8, 189.7, 176.2, 169.5, 189.9, 173.8, 178.7, 164.6, 166.0, 181.9, 164.3, 184.5, 181.4, 174.9, 176.9, 172.2, 168.9, 179.0, 189.8, 188.4, 175.2, 162.7, 192.9, 169.5, 179.1, 176.4, 179.7, 178.0, 179.8, 180.9, 183.0, 170.1, 171.5, 183.1, 179.7, 188.3, 171.6, 184.1, 184.8, 178.3, 183.1, 174.9, 180.9, 184.3, 170.8, 186.4, 171.5, 201.0, 172.0, 178.4, 179.8, 169.4, 173.5, 176.5, 172.5, 181.2, 179.1, 175.7, 185.3, 169.0, 178.1, 178.0, 170.6, 177.5, 183.1, 180.0, 172.3, 176.7, 190.2, 184.2, 179.0, 166.9, 168.4, 189.3, 180.4, 187.5, 181.7, 177.4, 179.0, 173.3, 169.8, 179.8, 181.1, 192.4, 177.2, 184.4, 200.0, 174.3, 186.8, 170.8, 181.8, 178.3, 165.3, 182.8, 184.9, 178.1, 177.1, 193.2, 191.3, 186.5, 162.2, 177.5, 182.5, 177.6, 168.3, 172.7, 168.5, 167.0, 167.5, 183.8, 160.6, 182.2, 179.9, 181.9, 175.2, 164.5, 169.3, 163.2, 186.0, 159.5, 181.8, 192.4, 181.1, 174.2, 170.7, 174.6, 193.3, 175.2, 171.2, 186.0, 195.9, 186.0, 181.8, 189.4, 175.3, 185.7, 180.2, 168.5, 181.4, 169.6, 174.8, 178.7, 184.8, 182.1, 187.4, 170.1, 170.5, 198.3, 181.0, 185.6, 187.2, 204.5, 176.1, 178.9, 171.6, 187.7, 176.6, 177.0, 182.1, 177.8, 176.5, 186.8, 180.8, 181.4, 176.9, 177.1, 191.0, 171.2, 175.7, 173.3, 179.1, 160.3, 178.0, 168.8, 177.1, 177.0, 182.4, 181.4, 176.2, 180.6, 195.5, 187.1, 184.6, 179.8, 174.0, 175.8, 188.8, 180.2, 181.1]
oppdelinger=[150, 160, 170, 180, 190, 200, 210]

# for å få et finere plot kan vi style med nøkkelordene:
plt.suptitle("Histogrammer")
plt.subplot(2,2,1)
plt.title("oppdelinger")
plt.hist(hoyder,bins=oppdelinger, color="seagreen", edgecolor="black")
plt.xlabel("Høyde (cm)")
plt.ylabel("Antall")
# plt.show()
# color="seagreen", edgecolor="black"

## OPPGAVER ##
# 1. oppgave Tegn et histogram med oppdelingene. 
# 2. oppgave Tegn et histogram med 20 oppdelinger.
# 3. oppgave Tegn et kumulativt histogram med oppdelingene.
# 4. oppgave Tegn et histogram med ulike størrelser på oppdelinger.
    #hint Bruk density=true for å få riktig fordeling.
# 5. oppgave Tegn alle disse 4 histogrammene i samme plot ved å bruke subplots
plt.subplot(2,2,2)
plt.hist(hoyder,cumulative=True, bins=oppdelinger, color="seagreen", edgecolor="black")
plt.xlabel("Høyde (cm)")
plt.ylabel("Antall")
plt.title("Kumulativ fordeling")
# plt.show()
plt.subplot(2,2,3)
plt.hist(hoyder, bins=20, color="seagreen", edgecolor="black")
plt.xlabel("Høyde (cm)")
plt.ylabel("Antall")
plt.title("20 bins fordeling")
# plt.show()

plt.subplot(2,2,4)
plt.hist(hoyder, bins=[0,150,180,200,210,220], color="seagreen", edgecolor="black")
plt.xlabel("Høyde (cm)")
plt.ylabel("Antall")
plt.title("5 bins fordeling")

plt.tight_layout()
plt.show()