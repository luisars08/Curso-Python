from tkinter import *

root = Tk()

myFrame = Frame(root, width=1000, height=550)
myFrame.pack()

cuadroTextoNombre=Entry(myFrame)
cuadroTextoNombre.grid(row=0,column=1)
cuadroTextoNombre.config(fg="red")

cuadroTextoApellido=Entry(myFrame)
cuadroTextoApellido.grid(row=1,column=1)

cuadroTextoMail=Entry(myFrame)
cuadroTextoMail.grid(row=2,column=1)

cuadroTextoDireccion=Entry(myFrame)
cuadroTextoDireccion.grid(row=3,column=1)

nombreLabelNombre=Label(myFrame, text="Nombre: ")
nombreLabelNombre.grid(row=0, column=0, sticky="w")

nombreLabelApellido=Label(myFrame, text="Apellido: ")
nombreLabelApellido.grid(row=1, column=0, sticky="w")

nombreLabelMail=Label(myFrame, text="Mail: ")
nombreLabelMail.grid(row=2, column=0, sticky="w")

nombreLabelDireccion=Label(myFrame,text="Direccion de casa: ")
nombreLabelDireccion.grid(row=3, column=0, sticky="w")

root.mainloop()