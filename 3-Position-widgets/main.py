from tkinter import *

root = Tk()
root.title("Position")
root.geometry("400x200")

def saludar():
    print('Hello!!')
    Label(text = "Greeting").pack()

def minimizar():
    root.iconify()

tagOne = Label(root, text = 'Greetings from here')
tagOne.place(x=30, y=50)

tagTwo = Label(root, text = 'Minimize from here')
tagTwo.place(x=30, y=100)

boton1 = Button(text = 'Click for greet', command = saludar)
boton1.place(x = 200, y = 50)

boton2 = Button(text = 'Click for Minimize', command = minimizar)
boton2.place(x = 200, y = 100)



root.mainloop()


# Introduction exercise
# tag = Label(root, text = 'tag')
# tag.grid(row = 0, column = 0)

# tag = Label(root, text = 'tag')
# tag.place(x = 100, y = 100)

# btnOne = Button(root, text = 'Button')
# btnOne.grid(row = 0, column = 1)