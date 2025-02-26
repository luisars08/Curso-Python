from io import open

archivo_externo = open("primerArchivo.txt","r+")

lista_archivo = archivo_externo.readlines()

lista_archivo[1] = "Hoy es Viernes y ya llegado el ansiado fin de semana \n"

archivo_externo.seek(0)

archivo_externo.writelines(lista_archivo)

archivo_externo.close()