from tkinter import *
root = Tk()
width = 700
height = 800
def apply():
    print(user_height_val.get())
    print(user_width_val.get())
    width =  user_height_val.get()
    height = user_width_val.get()
    root.geometry(f"{width}x{height}")
    
root.title("Auto Reshaper")

f1 = Frame(root,width= 800, height=100)
label = Label(f1,text = "Welcome to Auto Reshaper",font="lucid 25 bold italic").pack()
f1.pack()

user_height = Label(root, text= "Height", ).pack()
user_height_val =IntVar() 
user_height_entry = Entry(root,textvariable="Height", ).pack(padx=10, pady=10)


user_width  = Label(root, text= "Width").pack()
user_width_val  = IntVar() 
user_width_entry  = Entry(root,textvariable="Width").pack(padx=10, pady=10)

but = Button(root, text="Reshape",bg="blue", command=apply).pack()

root.mainloop()
