
def compararLista(lista1,lista2):

    if len(lista1) != len(lista2):
        return False
    else:
        for i in range(0,len(lista1)):
            if ( lista1[i] != lista2[i] ):
                return False
    return True


lista1 = ["Ana", "María", "Carla"]

lista2 = ["Ana", "María", "Carla"]
    
print( compararLista(lista1,lista2) )
