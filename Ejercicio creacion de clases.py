class CuentaCorriente():
    numeroCuenta = "0"
    titularCuenta = ""
    saldoCuenta = 0

    def __init__(self, numeroCuenta, titularCuenta, saldoCuenta):
        self.numeroCuenta  = numeroCuenta
        self.titularCuenta = titularCuenta
        self.saldoCuenta   = saldoCuenta

    def getDatos(self):
        
        return "El # cuenta es: " + self.numeroCuenta + " Nombre del Titular: " + self.titularCuenta + \
                 " Saldo de la cuenta: " + str(self.saldoCuenta)
    
    def ingresaDinero(self,monto):

        self.saldoCuenta=self.saldoCuenta+monto

        return self.saldoCuenta

    def retiraDinero(self,monto):

        self.saldoCuenta=self.saldoCuenta-monto

        return self.saldoCuenta

p1=CuentaCorriente("123", "Juan Díaz", 1000)

print(p1.getDatos())

print(p1.ingresaDinero(500))

print(p1.retiraDinero(700))

print(p1.getDatos())

