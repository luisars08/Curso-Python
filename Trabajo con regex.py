import re

lista_terminos = ["Ma1","Se1","Ma2","Va1","Ba1","Se2","Ma3","Ma4"]

for termino in lista_terminos:

    if re.findall("Ma[1-3]",termino):
        print(termino)

