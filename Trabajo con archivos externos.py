import os 

import io

#os.makedirs("PracticaDirectorio2")

os.chdir("PracticaDirectorio2")

os.rename("Ejemplo.txt", "ArchivoEliminar.txt")

print(os.getcwd())

print(os.listdir("./"))

