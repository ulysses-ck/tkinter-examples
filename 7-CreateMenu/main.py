from tkinter import *
# Config root
root = Tk()

barMenu = Menu(root)
root.config(menu=barMenu)

fileMenu= Menu(barMenu, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Close")
fileMenu.add_separator
fileMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(barMenu, tearoff=0)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")

helpMenu = Menu(barMenu, tearoff=0)
helpMenu.add_command(label="Help...")
helpMenu.add_separator()

barMenu.add_cascade(label="File", menu=fileMenu)
barMenu.add_cascade(label="Edit", menu=editMenu)
barMenu.add_cascade(label="Help", menu=helpMenu)

root.mainloop()