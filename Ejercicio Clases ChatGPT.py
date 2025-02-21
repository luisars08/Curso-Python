class Persona():
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print("Hola mi nombre es: ", self.nombre, " y tengo ", self.edad)
    
persona1 = Persona("Luis", 24)

persona1.presentarse()