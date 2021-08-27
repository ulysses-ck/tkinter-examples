from tkinter import *

root = Tk()
root.geometry("500x500")

products = Label(root,  text="Products", font="22")
products.pack()

def addProduct():
    listProduct.insert(END, entryOne.get())

listProduct = Listbox(root, width=50)
listProduct.insert(0, "Some 0")
listProduct.insert(1, "Some 1")
listProduct.insert(2, "Some 2")
listProduct.insert(3, "Some 3")
listProduct.insert(4, "Some 4")
listProduct.pack()

# Delete product
listProduct.delete(0)

entryOne = Entry(root, bd=10)
entryOne.pack()

btnOne = Button(root, text="Add product", command=addProduct)
btnOne.pack()

root.mainloop()