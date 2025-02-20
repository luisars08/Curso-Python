import math

print("Halla la raíz cuadrada")

numero= int( input("Dame un número: "))

intentos = 1

while numero<0:

    print("El número no puede ser negativo")
    numero= int( input("Dame un número: "))
    intentos = intentos+1

    if intentos==3:
        break

if intentos==3:
    print("Salio por exceso de intetnos")
else:
    raiz = math.isqrt(numero)
    print("La raiz de " + str(numero) + "es: " + str(raiz))