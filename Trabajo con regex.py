import re

lista_terminos = ["Ma:1","Se1","Ma2","Va1","Ba1","Se2","Ma.3","Ma4","Se:3","SeA","SeB","Va2","SeC"]

for termino in lista_terminos:

    if re.findall("Ma[.:]",termino):
        print(termino)

