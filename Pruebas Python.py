def minimo(lista):

    min_num = lista[0]

    for numero in lista:
        if min_num > numero:
            min_num = numero
         
    return min_num

def maximo(lista):
    
    max_num = lista[0]

    for numero in lista:
        if max_num < numero:
            max_num = numero
         
    return max_num

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

lista=[4,6,2,1,9,63,-134,566]
#lista = [5]
#lista = [42, 54, 65, 87, 0] 
#lista = [-52, 56, 30, 29, -54, 0, -110] 
print(minimo(lista))
print(maximo(lista))

print(minimum(lista))
print(maximum(lista))