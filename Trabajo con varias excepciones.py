def divide():

    try:

        op1= (float ( input("Introduce el primer número: ")))

        op2 = (float( input("Introduce el segundo número: ")))

        print( "El resultado es: " + str(op1/op2) )

    except ZeroDivisionError:

        print("No se puede dividir por 0")

    except ValueError:

        print("El valor introduccido no es númerico")

divide()

print("Cálculo finalizado. Continua el programa...")