from io import open

archivo_prueba = open("primerArchivoTarea.txt", "r")

lineas = archivo_prueba.readlines()

archivo_prueba.close()

palabra = "Un recuerdo invade mi mente."
palabra = "noche"
#print(lineas[0])

for parrafo in lineas:
    if palabra in parrafo:
        break
    print(parrafo)
