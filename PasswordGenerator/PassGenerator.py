#in this project we'll use the 3 modules and the  create an window using tkinter then add widgets to it and to function for generating password and copying to clipboard 


from tkinter import *
import pyperclip
import random

m=Tk()
m.title("passGen")
m.geometry("500x500")

passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    password = ""

    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    passstr.set(password)

def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

Label(m, text="Password Generator Application", font="calibri 20 bold").pack()#it organizes the widget into blocks
Label(m, text="Enter password length").pack(pady=3)
Entry(m, textvariable=passlen).pack(pady=3)
Button(m, text="Generate Password", command=generate).pack(pady=7)
Entry(m, textvariable=passstr).pack(pady=3)
Button(m, text="Copy to clipboard", command=copytoclipboard).pack()



m.mainloop()

