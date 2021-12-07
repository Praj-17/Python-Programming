from tkinter import *



"""
What is a frame??
When we want to divide the whole gui development process into 
small differnt parts, each part is called as a frame.
as you can see in the Vscode application GUI , the upper tab with file names ia a frame, 
the left side tab wih diffenrt ioptions is a frame likewise we can peprepare various frames.
"""
root = Tk()
root.title("watch out frames here")
root.geometry("655x333")

f1 = Frame(root, bg = "grey", borderwidth= 6, relief= SUNKEN)
f1.pack(side=LEFT,fill ="y", anchor="n")

l = Label(f1,text="Project Tkinter")
l.pack(side = TOP, pady = 142,anchor="n")

f2 = Frame(root, bg = "grey", borderwidth= 8, relief= SUNKEN)
f2.pack(side = TOP, fill = "x")
l1 = Label(f2, text="Welcome to VSCode",font="Helvetica 10 bold" )
l1.pack(side = TOP, pady = 5,anchor="n")





root.mainloop() 
  