
def prom(lista):

    if len(lista) == 0:
        return 0
    return sum(lista)/len(lista)

def find_average(array):
    return sum(array) / len(array) if array else 0

lista = [10,10,10]
#lista = []

print(find_average(lista))