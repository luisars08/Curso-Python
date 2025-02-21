from bs4 import BeautifulSoup

import requests

miDoc= requests.get("https://www.python.beispiel.programmierenlernen.io/")

docFinal = BeautifulSoup(miDoc.text,"html.parser")


titulo = docFinal.select(".card-title span")
print(titulo[1].text)

for imagen in docFinal.select(".card-block img"):
    print(imagen.attrs["src"])



print("----------------")



for iconos in docFinal.select(".emoji"):
    print(iconos.text)
    print("")

for titulo in docFinal.select(".card-title span"):
    print(titulo)
    print("")

for cuerpoTexto in docFinal.select(".card-text"):
    print(cuerpoTexto.text)
    print(" ")

for srcImagen in docFinal.select(".card-block img"):
    print(srcImagen.attrs["src"])
    print("")