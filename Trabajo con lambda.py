
mi_lista = [(11,5),(15,7),(2,4),(15,19),(8,4)]

"""def ordena_lista(t):
    return t[0]+t[1]"""

mi_lista.sort(key=lambda t:t[0]+t[1])

print(mi_lista)