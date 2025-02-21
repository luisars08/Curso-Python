from bs4 import BeautifulSoup
import requests

def urlWeb(link):
    dirWeb = requests.get(link)
    return dirWeb

def docWeb(dirWeb):
    documento = BeautifulSoup.select(dirWeb.text,"html.parser")
    return documento

def buscaImagen(valor):
    for imagen in docFinal.select(valor):
        print(imagen.attrs["src"])

def buscaTexto(valor):
    for parrafo in docFinal.select(valor):
        print(parrafo.text)

def buscaTitulo(valor):
    for titulo in docFinal.select(valor):
        print(titulo.text)

www = urlWeb("https://www.python.beispiel.programmierenlernen.io/")
docFinal = BeautifulSoup(www.text,"html.parser") #falta POO
bloqueImagen = ".card-block img"
bloqueParrafo = ".card-text"
bloqueTitulo = ".card-title span"
#buscaImagen(bloqueImagen)
#buscaTexto(bloqueParrafo)
buscaTitulo(bloqueTitulo)



