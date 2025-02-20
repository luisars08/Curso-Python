class Vehiculo():
    
    def __init__(self, color, ruedas, ancho, alto, asientos):
        
        self.color = color
        self.ruedas = ruedas
        self.ancho = ancho
        self.alto = alto
        self.asientos = asientos

        self.acelerando = False
        self.frenando = False
        self.girando = False
        self.retrocediendo = False

    def acelerar(self):
        self.acelerando = True

    def frenar(self):
        self.frenando = True

    def girar(self):
        self.girando = True

    def retroceder(self):
        self.retrocediendo = True

class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, ancho, alto, asientos, cilindrada, marchas, aireAcondicionado):
        super().__init__(color, ruedas, ancho, alto, asientos)

        self.cilindrada = cilindrada
        self.marcha = marchas
        self.aireAcondicionado = aireAcondicionado

        self.arrancado = False
        self.acelerado = False


    def arrancar(self):
        return "Rstoy arrancado"
    
    def acelerar(self):
        return super().acelerar()
    
    def frenar(self):
        return super().frenar()
    
    def girar(self):
        return super().girar()
    
    def retroceder(self):
        return super().retroceder()

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,ancho, alto, asientos):
        super().__init__(color,ruedas,ancho,alto,asientos)

        self.saltando=False
        self.derrapando=False

    def Saltar(self):
        self.saltando = True

    def Derrapar(self):
        self.derrapando = True

class Furgoneta(Coche):
    def __init__(self, color, ruedas, ancho, alto, asientos, cilindrada, marchas, aireAcondicionado, carga):
        super().__init__(color, ruedas, ancho, alto, asientos, cilindrada, marchas, aireAcondicionado)

        self.carga = carga

    def Cargar(self):
        self.carga = True

class Moto(Bicicleta,Coche):
    
    def __init__(self, color, ruedas, ancho, alto, asientos,cilindrada, marchas, aireAcondicionado):
        Bicicleta.__init__(color, ruedas, ancho, alto, asientos)
        Coche.__init__(self, color, ruedas, ancho, alto, asientos, cilindrada, marchas, aireAcondicionado)

    def Saltar(self):
        return super().Saltar()
    
    def Derrapar(self):
        return super().Derrapar()