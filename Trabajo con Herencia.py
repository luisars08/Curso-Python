class Persona(): #Primero es crear la clase. En este caso la clase Persona

    def __init__(self,nombre,apellido,edad): #Defnir las propiedades. En este caso en un constructor. El constructor le da un estado incial a las personas
        
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def getDatosPersonales(self): #Crear un método que devuelva la informacion. Un GETTER
        
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)

    def habla(self):     #Definir los comportamientos. ¿Qué puede hacer una persona?

        return "Estoy hablando"
    
    def piensa(self):
        
        return "Estoy pensando"
    
    def camina(self):
        
        return "Estoy caminando"
    
    def come(self):
        
        return "Estoy comiendo"
    
class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, escuela):
        
        super().__init__(nombre, apellido, edad)

        self.escuela = escuela

    def getDatosPersonales(self):

        return super().getDatosPersonales() + " Escuela: " + self.escuela

    def estudia(self):

        return "Estoy estudiando"
    
    
persona1 = Persona("Ana" , "Gomez", 35)    #Crear una instancia u objeto

estudiante1 = Estudiante("Juan", "Díaz", 21, "Ateneo de Mérida") 

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())