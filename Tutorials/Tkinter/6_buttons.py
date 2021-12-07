from tkinter import *
root = Tk()
root.geometry("655x333")

frame = Frame(root, borderwidth= 6, bg = "grey", relief= SUNKEN)
frame.pack(side=LEFT, anchor="nw")
"""

Button is any that thing which reacts or does something when you click it
for example the buttons that upu see in the upper right corner of your dialogue box 
for max, min and close are alos buttons
Arguments

The first argument is the frame where you are attaching the frame
the seconf argumet is the font color 
3 is text
4 is the command that you want to give it takes the function name as the fucntion(without parenthesis)

One more thing to note here is that while implemeting
the buttons the side is always inverted as you see here 
right means left and left means right





Implementing buttons
"""
def hello():
    print("Welcome to the buttons")
b1 = Button(frame, fg="red", text="print now", command=hello)
b1.pack(side= LEFT, padx=3)
b1 = Button(frame, fg="red", text="print now")
b1.pack(side= LEFT, padx=3)
b1 = Button(frame, fg="red", text="print now")
b1.pack(side= LEFT, padx=3)
b1 = Button(frame, fg="red", text="print now")
b1.pack(side= LEFT, padx=3)
b1 = Button(frame, fg="red", text="print now")
b1.pack(side=LEFT, padx=3)
b1 = Button(frame, fg="red", text="print now")
b1.pack(side= LEFT, padx=3)
b1 = Button(frame, fg="red", text="print now")
b1.pack(side= LEFT, padx=3)



# gui logic
root.mainloop() 