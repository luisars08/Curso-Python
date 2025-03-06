from tkinter import *

root = Tk()

myFrame = Frame(root, width=750, height=550)
myFrame.pack()

nombreLabel = Label(myFrame,text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky=W)

cuadroTexto = Entry(myFrame)
cuadroTexto.grid(row=0, column=1)
cuadroTexto.config(fg="red")

apellidoLb = Label(myFrame,text="Apellido: ").grid(row=1,column=0, sticky=W)
apellidoEt = Entry(myFrame)
apellidoEt.grid(row=1,column=1)
apellidoEt.config(fg="red")

mailLb = Label(myFrame,text="Mail: ").grid(row=2,column=0, sticky=W)
mailEt = Entry(myFrame).grid(row=2,column=1)

direccionLb = Label(myFrame,text="Dirección del domicilio: ").grid(row=3,column=0, sticky=W)
direccionEt = Entry(myFrame).grid(row=3,column=1)


root.mainloop()