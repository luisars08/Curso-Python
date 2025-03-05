def suma_array(lista):
    contador = 0
    for num in lista:
        if num > 0:
            contador+=num
    return contador

def positive_sum(arr):
    return sum(x for x in arr if x > 0)
        


lista_numeros = [1, -4, 7, 12]

print(suma_array(lista_numeros))