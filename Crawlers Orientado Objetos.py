from bs4 import BeautifulSoup

import requests


class PostCrawler():

    def __init__(self, titulo, emoticono, contenido, imagen):

        self.titulo    = titulo
        self.emoticono = emoticono
        self.contenido = contenido
        self.imagen    = imagen


class PostExtractor():

    def extraeInfo(self):

        miDoc = requests.get("https://www.python.beispiel.programmierenlernen.io/")

        docFinal = BeautifulSoup(miDoc.text, "html.parser")

        posts=[]

        for card in docFinal.select(".card"):
            titulo    = card.select(".card-title span")[1].text
            emoticono = card.select_one(".emoji").text
            contenido = card.select_one(".card-text").text
            imagen    = card.select_one("img").attrs["src"]

            crawled = PostCrawler(titulo, emoticono, contenido, imagen)
            posts.append(crawled)

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