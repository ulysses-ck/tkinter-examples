from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x4000")

# Example
w = Spinbox(root, values=("Python", "PHP", "Javascript", "Java"))
w.pack()

e = Spinbox(root, values=("Meat", "Vegetable", "Pastas"))
e.pack()

root.mainloop()