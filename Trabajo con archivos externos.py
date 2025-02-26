from io import open

archivo_externo = open("primerArchivo.txt","r")

#archivo_externo.write("\nGuardamos información de forma permanente")

informacion_lineas = archivo_externo.readlines()

archivo_externo.close()

print(informacion_lineas[1])