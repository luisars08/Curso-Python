from tkinter import *

from moduloCalculadora.Operaciones_Calculadora import *

def construit_botones(self,botones,filas_botones):

    contador = 0

    for fila in range(2,filas_botones+2):
        for columna in range(4):
            botones[contador].grid(row = fila, column = columna)
            contador += 1

def colocar_Boton(self, valor, mostrar=True, ancho = 9, alto = 1):
    return Button(self.ventana, text=valor, width=ancho, height= alto, font=("Helvetica", 9), 
    command=lambda:pulsasiones_teclas(self,valor,mostrar))