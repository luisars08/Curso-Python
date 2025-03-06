from tkinter import * 

raiz = Tk()

raiz.title("Primera ventana Py")

raiz.resizable(1,1)

raiz.iconbitmap("favicon.ico")

#raiz.geometry("700x400") Ya no es necesario porque ahora toma el tamaño del frame

raiz.configure(bg="#008491")

miFrame = Frame() #Programando el Frame

miFrame.pack(expand="True" ,fill="y")  #Empaquetando

miFrame.config(bg="red") #Darle color al Frame

miFrame.config(width="650", height="350")

raiz.mainloop()

