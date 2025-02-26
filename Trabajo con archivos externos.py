from io import open

archivo_externo = open("primerArchivo.txt","w")

archivo_externo.write("Bienvenidos a los archivos externos")

archivo_externo.close()