import matplotlib.pyplot as plt
import numpy as np
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
antallGutter = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]
antallJenter = [352, 268, 7286, 1028, 709, 851, 243, 826, 200, 895]
plt.figure(figsize=(10,5))
plt.subplots_adjust(left=0.4)
# plt.bar(utdanningsprogram,antall)
y=np.arange(len(utdanningsprogram))
plt.barh(y+0.2,antallGutter,0.4, label="Gutter", )
plt.barh(y-0.2,antallJenter,0.4, label="Jenter")
plt.legend()
plt.title("Søkertall fordelt på yrkesrettede utdanningsprogrammer i 2021")
plt.yticks(y,utdanningsprogram)
plt.grid(axis="x")
plt.show()