from tkinter import *
from PIL import Image, ImageTk
root = Tk()
#________________________________________________
root.geometry("455x244")
photo = PhotoImage(file="1.png")
picture = Label(image=photo)
picture.pack()
#_________________
"""
the .jpg images are currently not supported by tkinter to solve this problem we need to import thr pillow module and then process it acc to the following function
"""
image = Image.open("1.jpg")
photo = ImageTk.PhotoImage(image)

#this is mandatory step for evry photo you add
pic = Label(image= photo)
pic.pack()


# ___________________________________________________
root.mainloop()