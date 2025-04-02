from tkinter import *

from tkinter import messagebox as Mb

root = Tk()

myFrameRes = Frame(root,width=320, height=70)
myFrameRes.pack()

operacion = ""

operador1 = 0

variableResultado = StringVar()

entResultado = Entry(myFrameRes, textvariable=variableResultado)
entResultado.place(x=0, y=40)
entResultado.config(fg="black", font = "Arial 15" )

myFrame = Frame(root, width=1000, height=550)
myFrame.pack()



def btnNummero(num):    
    #variableResultado.set(variableResultado.get() + num)
    
    if  variableResultado.get() == "00":
        variableResultado.set("")

    elif variableResultado.get() == "..":
        variableResultado.set("")
        
    elif ".." in variableResultado.get():
        variableResultado.set("")
        #variableResultado.set("0")

    else:
        variableResultado.set(variableResultado.get() + num)
        
def suma():
    
    global operacion, operador1

    operacion = "suma" 

    operador1 = variableResultado.get()

    #Mb.showinfo("Valor capturado", operador1)

    int(operador1)

    operador1 += operador1

    Mb.showinfo("SUMA",operador1)

    variableResultado.set("")


    



btn1 = Button(myFrame, text=1, command=lambda:btnNummero("1"))
btn1.grid(row=2, column=0)
btn1.config(width=10,height=5)

btn2 = Button(myFrame, text=2, command=lambda:btnNummero("2"))
btn2.grid(row=2, column=1)
btn2.config(width=10,height=5)

btn3 = Button(myFrame, text=3, command=lambda:btnNummero("3"))
btn3.grid(row=2, column=2)
btn3.config(width=10,height=5)

btn4 = Button(myFrame, text=4, command=lambda:btnNummero("4"))
btn4.grid(row=1, column=0)
btn4.config(width=10,height=5)

btn5 = Button(myFrame, text=5, command=lambda:btnNummero("5"))
btn5.grid(row=1, column=1)
btn5.config(width=10,height=5)

btn6 = Button(myFrame, text=6, command=lambda:btnNummero("6"))
btn6.grid(row=1, column=2)
btn6.config(width=10,height=5)

btn7 = Button(myFrame, text=7, command=lambda:btnNummero("7"))
btn7.grid(row=0, column=0)
btn7.config(width=10,height=5)

btn8 = Button(myFrame, text=8, command=lambda:btnNummero("8"))
btn8.grid(row=0, column=1)
btn8.config(width=10,height=5)

btn9 = Button(myFrame, text=9, command=lambda:btnNummero("9"))
btn9.grid(row=0, column=2)
btn9.config(width=10,height=5)

btn0 = Button(myFrame, text=0, command=lambda:btnNummero("0"))
btn0.grid(row=3, column=1)
btn0.config(width=10,height=5)

btnPunto = Button(myFrame, text=".", command=lambda:btnNummero("."))
btnPunto.grid(row=3, column=0)
btnPunto.config(width=10, height=5)

btnIgual = Button(myFrame, text="=")
btnIgual.grid(row=3, column=2)
btnIgual.config(width=10, height=5)

btnDivision = Button(myFrame, text="/")
btnDivision.grid(row=0, column=3)
btnDivision.config(width=10, height=5)

btnMultiplica = Button(myFrame, text="x")
btnMultiplica.grid(row=1,column=3)
btnMultiplica.config(width=10, height=5)

btnResta = Button(myFrame, text="-")
btnResta.grid(row=2, column=3)
btnResta.config(width=10, height=5)

btnSuma = Button(myFrame, text="+", command= lambda:suma())
btnSuma.grid(row=3, column=3)
btnSuma.config(width=10, height=5)




root.mainloop()