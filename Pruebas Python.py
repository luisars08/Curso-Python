nombrePersonas = []

def agregarNOmbre(lista, nombreIntroducido):
    try:
        if nombreIntroducido in lista:
            raise ValueError
        else:
            lista.append(nombreIntroducido)
    except ValueError:
        print("Error. Este nombre ya esta introducido",nombreIntroducido)

introduccidos = 1

while introduccidos<11:
    nombre=input("Escrine un nombre: ")
    agregarNOmbre(nombrePersonas,nombre)
    introduccidos+=1

print( nombrePersonas)
