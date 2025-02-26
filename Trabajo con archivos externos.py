from io import open

archivo_externo = open("primerArchivo.txt","a")

archivo_externo.write("\nGuardamos información de forma permanente")

archivo_externo.close()