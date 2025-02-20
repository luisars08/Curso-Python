
def ValidaUsuarios(usuario):
    
    if len(usuario) < 5:
        print("El usuario no puede tener menos de 5 caracteres")

    elif len(usuario) > 15:
        print("El usuario no puede tener más de 15 caracteres")

    elif usuario.isalnum() == False: 
        print("El usuario solo puede contener letras y números”")

    else:

        return True 

def ValidaPass(password):

    if len(password) < 10:
        print("La contraseña debe tener más de 10 caracteres")
        return False

    elif password.isalnum():
        print("La contraseña debe contener un carácter que no sea ni letra ni número")
        return False
    
    elif any(caracter.isupper() for caracter in password) == False or any(letra.islower() for letra in password) == False:
        print("La contraseña no es segura")
        return False
    
    elif password.find(" ") > -1:
        print("La contraseña no puede contener espacios en blanco")
        return False

    else:
        return True
