from tkinter import *
import time

root = Tk()
root.title('My first Window made in tkinter')
root.geometry("500x300")

def printing():
    label1 = Label(root, text = 'Printing...')
    label1.pack()
    print("Printing ...")

btnOne = Button(root, text = 'Minimize', command = root.iconify, bg = "green", font= "Consolas")
btnOne.pack(side = RIGHT)

btnTwo = Button(root, text = 'Printing', command = printing, bg = "yellow", font= "Consolas")
btnTwo.pack(side = LEFT)

root.mainloop()