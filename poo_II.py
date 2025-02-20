class Persona():
    __nombre=""
    apellido=""
    __edad=0
    genero="sin definir"

    def __init__(self, nombre, apellido, genero):
        self.__nombre = nombre
        self.apellido = apellido
       
        self.genero = genero

    def setEdad(self,laEdad):  #Esto es un setter

        if laEdad<0 or laEdad>100:
            print("Error en la edad")
        else:
            self.__edad=laEdad
            return self.__edad

    def habla(self):
        
        return "La persona que se llama " + self.__nombre + " esta hablando"
    
    def caminar(self):
        
        return "La persona que se llama " + self.__nombre + " está caminando"

    def getDatos(self):  #Esto es un getter

        return "Nombre: " + self.__nombre + " Apellido: " + self.apellido + \
            " Edad: " + str(self.__edad) + " Género: " + self.genero
    

p1=Persona("Juan","Díaz","masculino")

p1.setEdad(102)

print(p1.getDatos())

p1.nombre="Alicia"

print(p1.getDatos())