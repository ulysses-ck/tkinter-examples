import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

root = tk.Tk()
# tk.BOLD === 'bold'

# var to stock the infotmation of
con40 = tkFont.Font(family = 'Consolas', size = 40, weight = tkFont.BOLD)
con20 = tkFont.Font(family = 'Consolas', size = 20, weight = tkFont.BOLD)

def select(option):
    ttk.Label(root, text = option, font = con20).pack()
    print(option)
ttk.Label(root, text = 'What is the best language?', font = con20).pack()
ttk.Button(root, text = 'Python', width = 200,  command = lambda: select("Python")).pack()
ttk.Button(root, text = 'Java', width = 200,  command = lambda: select("Java")).pack()
ttk.Button(root, text = 'Javascript', width = 200,  command = lambda: select("Javascript")).pack()

root.mainloop()