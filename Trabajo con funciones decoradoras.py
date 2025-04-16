def funcion_decoradora(funcion_parametro):

    def funcion_interna(*args):

        print("A continuación voy a realizar un cálculo")

        funcion_parametro(*args)

        print("Ya he terminado el trabajo")

    return funcion_interna




@funcion_decoradora
def suma(num1,num2):

    print(num1+num2)

@funcion_decoradora
def resta(num1,num2):

    print(num1-num2)


suma(5,7)

resta(20,5)