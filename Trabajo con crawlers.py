from bs4 import BeautifulSoup

import requests

miDoc= requests.get("https://www.python.beispiel.programmierenlernen.io/")

docFinal = BeautifulSoup(miDoc.text,"html.parser")


for iconos in docFinal.select(".emoji"):
    print(iconos.text)
    print("")

for titulo in docFinal.select(".card-title .emoji span"):
    print(titulo)
    print("")

for cuerpoTexto in docFinal.select(".card-text"):
    print(cuerpoTexto.text)
    print(" ")

for srcImagen in docFinal.select(".card-block img"):
    print(srcImagen.attrs["src"])
    print("")