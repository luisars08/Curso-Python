class Empleado():
    def __init__(self,nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def mostrarInfo(self):
        return "Nombre: " + self.nombre + " Sueldo: " + str(self.sueldo)
    
class Gerente(Empleado):

    def __init__(self,nombre,sueldo,departamento):

        super().__init__(nombre,sueldo)

        self.departamento = departamento

    def mostrarInfo(self):
        return super().mostrarInfo() + " Departamento: " + self.departamento
    
p1 = Empleado("Luis", 10000)
p2 = Gerente("Ars", 20000, "CEO")

print(p1.mostrarInfo())
print(p2.mostrarInfo())