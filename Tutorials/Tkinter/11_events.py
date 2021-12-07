from tkinter import *
root = Tk()
root.geometry("644x334")
root.title("Events")

def func(event):
    print(f"You clicked the button {event.x}, {event.y}")
    #x,y are w.r.t to the main screen

widget = Button(root, text = "Click me please")
widget.pack()

widget = widget.bind('<Button-1>', func)
# gui logic
root.mainloop()