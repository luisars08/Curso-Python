from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=450)

miFrame.pack()

#miLabel = Label(miFrame, text="Hoy son los Santos Inocentes")

#miLabel.place(x=120, y=125)

miLogo = PhotoImage(file="cat.gif")

#Label(miFrame, text="Hola soy Luis", fg="#008491",font=("Courier",20)).place(x=120,y=125)

Label(miFrame, image=miLogo).place(x=120, y=125)

root.mainloop()