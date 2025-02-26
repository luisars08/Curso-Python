from io import open

archivo_externo = open("primerArchivo.txt","r")

print(archivo_externo.read())

archivo_externo.seek(0)

print(archivo_externo.read())
