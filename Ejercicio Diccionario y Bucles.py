
paises = {}

pais = input("Escribe el nombre de un pais: ")

while pais != "salir":
    
    ciudad = input("Escribe el nombre de una ciudad: ")

    lista_ciudades = paises.setdefault(pais,[ciudad])

    if lista_ciudades != ciudad:

        paises[pais].append(ciudad)

    pais = input("Escribe el nombre de un pais: ")

print(paises)