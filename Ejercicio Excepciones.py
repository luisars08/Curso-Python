
listaNombre=[]

def defineNombres(nombre):
        
    if nombre in listaNombre:
        raise ValueError("Error. Este nombre ya se ha introducido")
    else:
        listaNombre.append(nombre)    

for i in range(0,10):
    
    nombre = input("Dame el nombre de una persona: ")    
    try:
        defineNombres(nombre)
    except ValueError:
        print("Error al introducir el nombre .. " + nombre)
        while nombre in listaNombre:
            nombre=input("Escribe un nombre que no este repetido: ")
            if nombre not in listaNombre:
                listaNombre.append(nombre)
                break

print(listaNombre)