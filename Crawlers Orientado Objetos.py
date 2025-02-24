from bs4 import BeautifulSoup

import requests

from urllib.parse import urljoin

import time


class PostCrawler():

    def __init__(self, titulo, emoticono, contenido, imagen):

        self.titulo    = titulo
        self.emoticono = emoticono
        self.contenido = contenido
        self.imagen    = imagen


class PostExtractor():

    def extraeInfo(self):

        urlBase = "https://www.python.beispiel.programmierenlernen.io/"

        posts=[]

        while urlBase!= "":

            miDoc = requests.get(urlBase)

            docFinal = BeautifulSoup(miDoc.text, "html.parser")

            time.sleep(2)

            for card in docFinal.select(".card"):
                titulo    = card.select(".card-title span")[1].text
                emoticono = card.select_one(".emoji").text
                contenido = card.select_one(".card-text").text
                imagen    = urljoin(urlBase,card.select_one("img").attrs["src"])

                crawled = PostCrawler(titulo, emoticono, contenido, imagen)
                posts.append(crawled)

            boton_siguiente = docFinal.select_one(".navigation .btn")

            if boton_siguiente:
                rutas_absolutas = urljoin(urlBase,boton_siguiente.attrs["href"])
                urlBase=rutas_absolutas
                print(rutas_absolutas)
            else:
                urlBase=""

        return posts

unPost = PostExtractor()

listaPost = unPost.extraeInfo()

for elPosts in listaPost:

    print(elPosts.emoticono)
    print(elPosts.titulo)
    print(elPosts.contenido)
    print(elPosts.imagen)
    print()
#print(listaPost)