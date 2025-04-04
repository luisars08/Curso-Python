import re

cadena="Estoy trabajando con Python en domingo y Semana Santa. El próximo domingo no pienso grabar ningún vídeo"

busqueda = "domingo"

print(len(re.findall(busqueda,cadena)))