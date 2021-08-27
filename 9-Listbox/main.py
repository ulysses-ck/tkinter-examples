from tkinter import *

root = Tk()
root.geometry("500x500")

products = Label(root,  text="Products", font="22")
products.pack()

listProduct = Listbox(root, width=50)
listProduct.insert(0, "Some 0")
listProduct.insert(1, "Some 1")
listProduct.insert(2, "Some 2")
listProduct.insert(3, "Some 3")
listProduct.insert(4, "Some 4")
listProduct.pack()


root.mainloop()