from tkinter import *

from tkinter import messagebox as MessageBox

root = Tk()

myFrame = Frame(root, width=1000, height=550)
myFrame.pack()

miVariable    = StringVar()
miVariableApe = StringVar()
miVariablePas = StringVar()
miVariableMai = StringVar()
miVariableDir = StringVar()


cuadroTextoNombre=Entry(myFrame, textvariable=miVariable)
cuadroTextoNombre.grid(row=0,column=1, padx=15, pady=15)
cuadroTextoNombre.config(fg="red")

cuadroTextoApellido=Entry(myFrame, textvariable=miVariableApe)
cuadroTextoApellido.grid(row=1,column=1, padx=15, pady=15)

cuadroTextoContra=Entry(myFrame, textvariable=miVariablePas)
cuadroTextoContra.grid(row=2,column=1, padx=15, pady=15)
cuadroTextoContra.config(show="*")

cuadroTextoMail=Entry(myFrame, textvariable=miVariableMai)
cuadroTextoMail.grid(row=3,column=1, padx=15, pady=15)

cuadroTextoDireccion=Entry(myFrame, textvariable=miVariableDir)
cuadroTextoDireccion.grid(row=4,column=1, padx=15, pady=15)

cuadroTextoOpiniones=Text(myFrame, width=15, height=10)
cuadroTextoOpiniones.grid(row=5, column=1, padx=15, pady=15)

miScrollVertical = Scrollbar(myFrame, command=cuadroTextoOpiniones.yview)
miScrollVertical.grid(row=5,column=2, sticky=NSEW)

cuadroTextoOpiniones.config(yscrollcommand=miScrollVertical.set)

nombreLabelNombre=Label(myFrame, text="Nombre: ")
nombreLabelNombre.grid(row=0, column=0, sticky="w")

nombreLabelApellido=Label(myFrame, text="Apellido: ")
nombreLabelApellido.grid(row=1, column=0, sticky="w")

nombreLabelContra=Label(myFrame, text="Password: ")
nombreLabelContra.grid(row=2, column=0, sticky="w")

nombreLabelMail=Label(myFrame, text="Mail: ")
nombreLabelMail.grid(row=3, column=0, sticky="w")

nombreLabelDireccion=Label(myFrame,text="Direccion: ")
nombreLabelDireccion.grid(row=4, column=0, sticky="w")

nombreLabelComentarios=Label(myFrame,text="Comentarios: ")
nombreLabelComentarios.grid(row=5, column=0, sticky="w")

def funcionBoton():
    
    #MessageBox.showinfo("Información rescatada", cuadroTextoNombre.get() + " " + cuadroTextoApellido.get() + " "  + cuadroTextoContra.get())
    cuadroTextoOpiniones.insert(INSERT, "Esto es una prueba de texto")

botonEnviar=Button(root, text="Enviar", command=funcionBoton)

botonEnviar.pack()


root.mainloop()