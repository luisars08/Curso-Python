class CuentaCorriente():

    def __init__(self, numeroCuenta, titularCuenta, saldoCuenta):
        self.numeroCuenta  = numeroCuenta
        self.titularCuenta = titularCuenta
        self.saldoCuenta   = saldoCuenta

    def getDatos(self):
        
        return "El # cuenta es: " + self.numeroCuenta + " Nombre del Titular: " + self.titularCuenta + \
                 " Saldo de la cuenta: " + str(self.saldoCuenta)
    
    def ingresar(self,monto):

        self.saldoCuenta=self.saldoCuenta+monto

        return self.saldoCuenta

    def retirar(self,monto):

        self.saldoCuenta=self.saldoCuenta-monto

        return self.saldoCuenta


class CuentaJoven(CuentaCorriente):
    
    def __init__(self, numeroCuenta, titularCuenta, saldoCuenta, bonus_promocion=0):
        super().__init__(numeroCuenta, titularCuenta, saldoCuenta)
        self.bonus_promocion = bonus_promocion
        self.saldoCuenta += bonus_promocion

    def getBonus(self):
        return self.bonus_promocion
    
    def ingresar(self, monto):
        return super().ingresar(monto)
    
    def retirar(self, monto):
        return super().retirar(monto)
    
    def getDatos(self):
        return super().getDatos() + " Bonus:" + str(self.bonus_promocion)

p1=CuentaCorriente("123", "Juan Díaz", 1000)
p1.ingresar(500)
p1.retirar(700)
print(p1.getDatos())

p2=CuentaJoven("564","Luis",15000,1000)
p2.ingresar(1000)
p2.retirar(500)
print(p2.getDatos())
print(p2.getBonus())

