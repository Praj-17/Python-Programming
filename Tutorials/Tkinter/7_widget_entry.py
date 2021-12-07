from tkinter import *
root = Tk()
root.geometry("655x333")

user = Label(root, text = "Username")
password = Label(root, text="Password")
user.grid()
password.grid(row =1)
"""
in this file we are studying how to take an input from the user

variable clasLabeses in tkinter
booleanVar, doubleVar, IntVar, StringVar


"""
def getvals():
    print(f"username = {uservalue.get()}")
    print(f"passname = {passvalue.get()}")
    
uservalue = StringVar()
passvalue = StringVar()

userentry  = Entry(root, textvariable= uservalue)
passentry  = Entry(root, textvariable= passvalue)

userentry.grid(row = 0, column=1)
passentry.grid(row = 1, column=1)

Button(text = "Submit", command=getvals).grid()
# gui logic
root.mainloop()