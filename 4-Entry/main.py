from tkinter import *

root = Tk()
root.title("Entry")
root.geometry("800x300")
root.resizable(0,0)

                                    # fontCustom = '[Font] [size]'
conReg20 = 'Comfortaa-Regular 20'   # You can select any font available font in your device
conReg40 = 'Comfortaa-Regular 40'   #
comBol10 = 'Comfortaa-Bold 10'      #

firstName = StringVar()
lastName = StringVar()
greet = StringVar()

firstName.set('John')
lastName.set('Doe')

def saludar():
    greet.set(f"Hi {firstName.get()} {lastName.get()}!")

tagOne = Label(root, text  = 'Write your First name: ', bd = 4, bg ='#38ffd1', font = (comBol10))
tagOne.place(x = 10, y = 10)
inputOne = Entry(root, textvariable = firstName)
inputOne.place(x = 170, y = 10)

tagTwo = Label(root, text  = 'Write your Last Name: ', bd = 4, bg ='#38ffd1', font = (comBol10))
tagTwo.place(x = 10, y = 40)
inputTwo = Entry(root, textvariable = lastName)
inputTwo.place(x = 170, y = 40)

btn = Button(root, text = 'Greet Now', command = saludar, bd = 4, bg ='#38ffd1', font = (comBol10))
btn.place(x = 10, y = 100)

inputThree = Entry(root, bd = 2, font = (comBol10), textvariable = greet, state = "disable", width = 90)
inputThree.place(x = 60, y = 210)

root.mainloop()