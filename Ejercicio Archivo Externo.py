from io import *

archivo = open("clientes.txt","r",encoding="UTF-8")

lineas = archivo.readlines()

archivo.close()

doc = []

for parrafo in lineas:
    
    linea = parrafo.split(";")

    docCliente = {"Código":linea[0], "Nombre":linea[1], "Dirección":linea[2], "Población":linea[3], "Teléfono":linea[4], "Responsable":linea[5]}

    doc.append(docCliente)

for c in doc:
    print("Código Articulo={} Nombre={} Dirección={} Población={} Teléfono={} Responsable={}"
            .format(c["Código"],c["Nombre"],c["Dirección"],c["Población"],c["Teléfono"],c["Responsable"]))