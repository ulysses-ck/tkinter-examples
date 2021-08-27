from tkinter import *

root = Tk()
root.title("Radiobutton")
root.geometry("400x300")
root.config(bg="goldenrod3")

def operacion():
    number = int(entrada1.get())
    if option.get()==1:
        total = number*5
    elif option.get()==2:
        total = number*10
    elif option.get()==3:
        total = number*20
    elif option.get()==4:
        total = number*30
    elif option.get()==5:
        total = number*40
    else:
        total = number * number
    print(f"Total of the operation is: {str(total)}")

option = IntVar()

etiqueta1 = Label(root, text="Write a number")
etiqueta1.place(x=20, y=20)

entrada1 = Entry(root)
entrada1.place(x=150, y=30)

etiqueta2 = Label(root, text="Elija la cantidad")
etiqueta2.place(x=20, y=50)

x5 = Radiobutton(root,text="x5", value=1, variable=option)
x5.place(x=20 ,y=80)

x10= Radiobutton(root,text="x10", value=2, variable=option)
x10.place(x=70 ,y=80)

x20= Radiobutton(root,text="x20", value=3, variable=option)
x20.place(x=120 ,y=80)

x30= Radiobutton(root,text="x30", value=4, variable=option)
x30.place(x=20 ,y=110)

x40= Radiobutton(root,text="x40", value=5, variable=option)
x40.place(x=70 ,y=110)

btnOne = Button(root, text="realizar operacion", command=operacion)
btnOne.place(x=20, y=140)

root.mainloop()