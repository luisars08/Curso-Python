import os 

import io

#os.makedirs("PracticaDirectorio2")

os.chdir("PracticaDirectorio2")

archivo_externo = open("Ejemplo.docx", "w")

archivo_externo.write("Texto de ejemplo...")

print(os.getcwd())

print(os.listdir("./"))

