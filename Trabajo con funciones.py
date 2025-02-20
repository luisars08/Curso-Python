def imprimeMensaje():
    return "Este es un mensaje de la función"

#print(imprimeMensaje())

def imprimeMensajePersonalizado(mensaje, valor1, valor2):
    return mensaje + str( (valor1+valor2) )

print( imprimeMensajePersonalizado("La suma es: ", 5, 7) )