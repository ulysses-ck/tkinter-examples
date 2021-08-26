from tkinter import *

root = Tk()
root.title("Posicionar")
root.geometry("400x200")

def saludar():
    print('Saludo')
    Label(text = "Saludo").pack()

def minimizar():
    root.iconify()

etiqueta1 = Label(root, text = 'Saludos from here')
etiqueta1.place(x=30, y=50)

etiqueta2 = Label(root, text = 'Minimizar desde aquí')
etiqueta2.place(x=30, y=100)

boton1 = Button(text = 'Click para Saludar', command = saludar)
boton1.place(x = 200, y = 50)

boton2 = Button(text = 'Click para Minimizar', command = minimizar)
boton2.place(x = 200, y = 100)



root.mainloop()


# Ejercicio de introduccion
# etiqueta = Label(root, text = 'Etiqueta')
# etiqueta.grid(row = 0, column = 0)

# etiqueta = Label(root, text = 'Etiqueta')
# etiqueta.place(x = 100, y = 100)

# boton1 = Button(root, text = 'Botón')
# boton1.grid(row = 0, column = 1)