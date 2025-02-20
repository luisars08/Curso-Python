import random

print("Bienvenido a mi juega un número al azar")

nmrRandom=random.randint(1,100)

intentos=1

nmr = int( input("Elije un número entre el 1 al 100 para ver si le atinas al que yo escojí: ") )

while nmr!=nmrRandom:
    if nmr < nmrRandom:
        print("Es un número mayor el que yo pensé.")

    if nmr > nmrRandom:
        print("Es un número menor el que yo pensé")

    nmr = int( input("Escoje otro número: ") )
    intentos = intentos +1

print("Felicidades el número que pensaba es (" + str(nmrRandom) + ") lo has adivinado en: " + str(intentos) + " intentos" )