import re

cadena="Estoy trabajando con Python en domingo y semana santa"

busqueda = "domingo"

texto_encontrado = re.search(busqueda,cadena)

print(texto_encontrado.start())

print(texto_encontrado.end())

print(texto_encontrado.span())