from tkinter import *

root = Tk()
root.title("Entrada")
root.geometry("800x300")
root.resizable(0,0)

conReg20 = 'Comfortaa-Regular 20'
conReg40 = 'Comfortaa-Regular 40'
comBol10 = 'Comfortaa-Bold 10'

nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

nombre.set('Escribe aquí tu nombre')
apellido.set('Escribe aquí tu apellido')

def saludar():
    saludo.set(f"Hola {nombre.get()} {apellido.get()}")

etiqueta1 = Label(root, text  = 'Escribe nombre aquí: ', bd = 4, bg ='#38ffd1', font = (comBol10))
etiqueta1.place(x = 10, y = 10)
campoUno = Entry(root, textvariable = nombre)
campoUno.place(x = 170, y = 10)

etiquetaDos = Label(root, text  = 'Escribe apellido aquí: ', bd = 4, bg ='#38ffd1', font = (comBol10))
etiquetaDos.place(x = 10, y = 40)
campoDos = Entry(root, textvariable = apellido)
campoDos.place(x = 170, y = 40)

boton = Button(root, text = 'Saludar ahora', command = saludar, bd = 4, bg ='#38ffd1', font = (comBol10))
boton.place(x = 10, y = 100)

campoTres = Entry(root, bd = 2, font = (comBol10), textvariable = saludo, state = "disable", width = 90)
campoTres.place(x = 60, y = 210)

root.mainloop()