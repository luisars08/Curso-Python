import re

cadena="Estoy trabajando con Python en domingo y semana santa"

busqueda = "domingo"

if re.search(busqueda,cadena) is not None:

    print("Se encontró el termino " , busqueda)

else:

    print("No se encontro el termino " , busqueda)