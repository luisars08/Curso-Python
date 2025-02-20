def generarPares(limite):

    num= 1

    while num<limite:

       yield num*2

       num += 1

sucesionPares = generarPares(6)
    
print(next(sucesionPares))

print("Ahora va el siguiente valor: ")

print(next(sucesionPares))

print("Ahora va el siguiente valor: ")

print(next(sucesionPares))

print("Ahora va el siguiente valor: ")

print(next(sucesionPares))

print("Ahora va el siguiente valor: ")

print(next(sucesionPares))

print("Ahora va el siguiente valor: ")