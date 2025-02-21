class CuentaBancaria():

    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,cantidad):
        self.saldo = self.saldo + cantidad
        return self.saldo
    
    def retirar(self,cantidad):
        self.saldo = self.saldo - cantidad
        return self.saldo
    
juan = CuentaBancaria("Juan Bodoque", 10000)

print(juan.depositar(100))

print(juan.retirar(100))