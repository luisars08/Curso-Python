from tkinter import *

root = Tk()

myFrameRes = Frame(root,width=320, height=100, background="gray")
myFrameRes.pack()

myFrame = Frame(root, width=1000, height=550)
myFrame.pack()

btn1 = Button(myFrame, text=1)
btn1.grid(row=2, column=0)
btn1.config(width=10,height=5)

btn2 = Button(myFrame, text=2)
btn2.grid(row=2, column=1)
btn2.config(width=10,height=5)

btn3 = Button(myFrame, text=3)
btn3.grid(row=2, column=2)
btn3.config(width=10,height=5)

btn4 = Button(myFrame, text=4)
btn4.grid(row=1, column=0)
btn4.config(width=10,height=5)

btn5 = Button(myFrame, text=5)
btn5.grid(row=1, column=1)
btn5.config(width=10,height=5)

btn6 = Button(myFrame, text=6)
btn6.grid(row=1, column=2)
btn6.config(width=10,height=5)

btn7 = Button(myFrame, text=7)
btn7.grid(row=0, column=0)
btn7.config(width=10,height=5)

btn8 = Button(myFrame, text=8)
btn8.grid(row=0, column=1)
btn8.config(width=10,height=5)

btn9 = Button(myFrame, text=9)
btn9.grid(row=0, column=2)
btn9.config(width=10,height=5)

btn0 = Button(myFrame, text=0)
btn0.grid(row=3, column=1)
btn0.config(width=10,height=5)

btnPunto = Button(myFrame, text=".")
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

btnSuma = Button(myFrame, text="+")
btnSuma.grid(row=3, column=3)
btnSuma.config(width=10, height=5)

root.mainloop()