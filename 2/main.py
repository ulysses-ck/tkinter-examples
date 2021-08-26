import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

root = tk.Tk()
# tk.BOLD === 'bold'

# var to stock the infotmation of 
con40 = tkFont.Font(family = 'Consolas', size = 40, weight = tkFont.BOLD)
con20 = tkFont.Font(family = 'Consolas', size = 20, weight = tkFont.BOLD)

def seleccionar(opcion):
    ttk.Label(root, text = opcion, font = con20).pack()
    print(opcion)
ttk.Label(root, text = 'What is the best language?', font = con20).pack()
ttk.Button(root, text = 'Python', width = 200,  command = lambda: seleccionar("Python"), fg = "blue").pack()
ttk.Button(root, text = 'Java', width = 200,  command = lambda: seleccionar("Java"), fg = "blue").pack()
ttk.Button(root, text = 'Javascript', width = 200,  command = lambda: seleccionar("Javascript"), fg = "blue").pack()

root.mainloop()