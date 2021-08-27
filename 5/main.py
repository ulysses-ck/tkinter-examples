from tkinter import *

root = Tk()
root.title("Radiobuttontons")
root.geometry("400x300")
root.config(bg="goldenrod3")

def operacion():
    numero = int(entrada1.get())
    if opcion.get()==1:
        total = numero*5
    elif opcion.get()==2:
        total = numero*10
    elif opcion.get()==3:
        total = numero*20
    elif opcion.get()==4:
        total = numero*30
    elif opcion.get()==5:
        total = numero*40
    else:
        total = numero * numero
    print(f"Total of the operation is: {str(total)}")

opcion = IntVar()

etiqueta1 = Label(root, text="Escriba u numero")
etiqueta1.place(x=20, y=20)

entrada1 = Entry(root)
entrada1.place(x=150, y=30)

etiqueta2 = Label(root, text="Elija la cantidad")
etiqueta2.place(x=20, y=50)

x5 = Radiobutton(root,text="x5", value=1, variable=opcion)
x5.place(x=20 ,y=80)

x10= Radiobutton(root,text="x10", value=2, variable=opcion)
x10.place(x=70 ,y=80)

x20= Radiobutton(root,text="x20", value=3, variable=opcion)
x20.place(x=120 ,y=80)

x30= Radiobutton(root,text="x30", value=4, variable=opcion)
x30.place(x=20 ,y=110)

x40= Radiobutton(root,text="x40", value=5, variable=opcion)
x40.place(x=70 ,y=110)

boton1 = Button(root, text="realizar operacion", command=operacion)
boton1.place(x=20, y=140)

root.mainloop()