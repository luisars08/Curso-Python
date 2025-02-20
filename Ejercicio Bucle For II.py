numero = int( input( "Dame el número con el que empezaré a contar los números primos: ") )

rango = int( input("Dame el número que será el límite para contar: ") )

def primos(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    print("Es primo " + str(num) )
    return True

for i in range(numero,rango):
    primos(i)
