
frase1="Los lunes son los mejores días para programar"  #45  4to
frase2="Python es moderno"                              #17  1ro
frase3="Veremos Inteligencia Artificial más adelante"   #44  3ro
frase4="Lambda simplifica el código"                    #27  2do

lista_frases = ["Los lunes son los mejores días para programar","Python es moderno","Veremos Inteligencia Artificial más adelante","Lambda simplifica el código" ]

'''def cuenta_letras(f):
    return len(f.split())

lista_frases.sort(key=cuenta_letras)'''

lista_frases.sort(key=lambda f:len(f.split()),reverse=True)

print("EL RESULTADO ES: ", lista_frases)