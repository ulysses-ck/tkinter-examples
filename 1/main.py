from tkinter import *
import time

root = Tk()
root.title('Mi primer ventana')
root.geometry("500x300")

def Imprimir():
    label1 = Label(root, text = 'Imprimiendo...')
    label1.pack()
    print("imprimiendo ...")

boton1 = Button(root, text = 'Minimizar', command = root.iconify, bg = "green", font= "Consolas")
boton1.pack(side = RIGHT)

boton2 = Button(root, text = 'Imprimir', command = Imprimir, bg = "yellow", font= "Consolas")
boton2.pack(side = LEFT)

root.mainloop()