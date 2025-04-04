import re

lista_terminos = ["camión", "camion", "niños","niñas","ejemplo"]

for termino in lista_terminos:

    if re.findall("niñ[ao]s",termino):
        print(termino)

