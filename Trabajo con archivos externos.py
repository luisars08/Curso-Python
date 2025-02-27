import os 

import io

#os.makedirs("PracticaDirectorio2")

os.chdir("PracticaDirectorio2")

os.remove("Ejemplo.docx")

os.chdir("../")

os.rmdir("PracticaDirectorio2")

#print(os.getcwd())

#print(os.listdir("./"))

