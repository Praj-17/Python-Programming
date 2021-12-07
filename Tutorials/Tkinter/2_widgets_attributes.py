from tkinter import *
root = Tk()

#This is where we are deciding the frame dimensions

# widthxheight
root.geometry("644x434")
root.minsize(300,100)
root.maxsize(1600,1200)

#adding a text the GUI
title = Label(text= "Welcome to my first GUI")
title.pack()


# gui logic
root.mainloop()