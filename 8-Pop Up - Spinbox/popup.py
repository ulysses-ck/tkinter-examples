from tkinter import *
from tkinter import messagebox

# Config root
root = Tk()

barMenu = Menu(root)
root.config(menu=barMenu)

def close():
    messagebox.askquestion("Close", message="Are you sure?")

def license():
    messagebox.showinfo("Version", message="Version 1.0")

def error():
    messagebox.showerror("¡CRITICAL ERROR!", "An unexpected error has occurred")

def warning():
    messagebox.showwarning("ATENTION", "The file will be removed if your continue. Save it before!")

fileMenu= Menu(barMenu, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open", command=warning)
fileMenu.add_command(label="Save", command=error)
fileMenu.add_command(label="Close", command=close)
fileMenu.add_separator
fileMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(barMenu, tearoff=0)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")

helpMenu = Menu(barMenu, tearoff=0)
helpMenu.add_command(label="License", command=license)
helpMenu.add_separator()

barMenu.add_cascade(label="File", menu=fileMenu)
barMenu.add_cascade(label="Edit", menu=editMenu)
barMenu.add_cascade(label="License", menu=helpMenu)

root.mainloop()