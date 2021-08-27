from tkinter import *

root = Tk()
root.config(bd=20, bg="goldenrod3")
root.title("Casa de comidas")

def orden():
    lista = ""
    if(queso.get()):
        lista += " Sin queso"
    else:
        lista += " Con queso"

    if(lechuga.get()):
        lista += " y sin lechuga"
    else:
        lista += " y con lechuga"
    imprimir.config(text=lista)

queso = IntVar()
lechuga = IntVar()

imagen = PhotoImage(file="extraburger.png")
Label(root, image=imagen).pack(side=LEFT)

frame = Frame(root)
frame.pack(side=RIGHT)
frame.config(bg="goldenrod3")
Label(frame, text="¿Como quieres tu hamburguesa?", bg="goldenrod3", font="28").pack(anchor="w")
Checkbutton(frame, text="Con queso", variable="queso", onvalue=1, offvalue=0, bg="goldenrod3", command=orden).pack(anchor="w")
Checkbutton(frame, text="Con lechuga", variable="lechuga", onvalue=1, offvalue=0, bg="goldenrod3", command=orden).pack(anchor="w")

imprimir = Label(frame, bg="goldenrod3", text="", font="Courier 22")
imprimir.pack()


root.mainloop()
