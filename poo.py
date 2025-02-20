class Coche():      #proppiedades/caracteristicas
    ruedas=4
    largoChasis=260
    anchoChasis=130
    arrancado=False

    def arrancar(self): #comportamiento/método
        self.arrancado = True

    def estadoCoche(self):
        if (self.arrancado):
            return "El coche esta en funcionamiento"
        else:
            return "El coche esta apagado"

mazda=Coche() #ejemplar de clase

renault = Coche()

print("Tu coche tiene: " + str(renault.ruedas) + " ruedas")

renault.arrancar()

print("Tu coche esta arrancado: " + str(renault.arrancado))

print(renault.estadoCoche())

print(mazda.estadoCoche())