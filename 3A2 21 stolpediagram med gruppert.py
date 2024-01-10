import matplotlib.pyplot as plt

utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

antall = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]

#forbedringer
plt.figure(figsize=(10,5))          # Størrelsen på figuren, 2x bred som høy
plt.subplots_adjust(left=0.4)       # Øker plass på venstre siden av diagramet

#plottet:
plt.ticklabel_format(scilimits=(0,10)) ## Angir hvor vi ikke skal bruke vitenskapelig notasjon i plottet

# plt.bar(utdanningsprogram,antall) # stående stolpediagram
plt.barh(utdanningsprogram,antall)  # liggende stolpediagram
plt.title("Søkertall fordelt på yrkesrettede utdanningsprogrammer i 2021")
plt.grid(axis="x")                  # Legger inn kun x-linjer
plt.show()


# Alternativ representasjon av input:

# utdanningsvalg = {
#   "Bygg- og anleggsteknikk": 3811, 
#   "Elektro og datateknologi": 4168,
#   "Helse- og oppvekstfag": 8661,
#   "Naturbruk": 2057,
#   "Restaurant- og matfag": 1484,
#   "Teknologi- og industrifag": 5501,
#   "Håndverk, design og produktutvikling": 313,
#   "Frisør, blomster, interiør og eksponeringsdesign": 901,
#   "Informasjonsteknologi og medieproduksjon": 1309,
#   "Salg, service og reiseliv": 2061
# }

# utdanningsprogram = list(utdanningsvalg.keys())
# antall = list(utdanningsvalg.values())

# gruppert stolpediagram
antallGutter = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]
antallJenter = [352, 268, 7286, 1028, 709, 851, 243, 826, 200, 895]
plt.figure(figsize=(10,5))  #avlang figur igjen
plt.subplots_adjust(left=0.4)

# plt.barh()
#Tar inputs
#     y: ArrayLike,             hvor hver "bar" plasseres i bredden
#     width: ArrayLike,         bredden på hver bar (verdien)
#     height: ArrayLike = 0.8,  høyden (tykkelsen)

import numpy as np #Dårlig praksis burde være på starten av filen
lengde=len(utdanningsprogram)
y=np.arange(lengde) #Fordeler tall fra 0 til lengden

plt.barh(y+0.2, antallGutter,0.4 , label="Gutter")
plt.barh(y-0.2, antallJenter,0.4 , label="Jenter")



plt.yticks(y,utdanningsprogram)
plt.legend()

plt.show()