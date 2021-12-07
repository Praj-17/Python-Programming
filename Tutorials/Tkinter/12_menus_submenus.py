from tkinter import *
root = Tk()
def myfunc():
    print("I am a command function")
root.geometry("733x566")
root.title("VSCode")


#Creating a menu
# mymenu = Menu(root)
# mymenu.add_command(label="file", command= myfunc)
# mymenu.add_command(label="Exit", command= quit)
# root.config(menu = mymenu)

#Creating a 
New_menu = Menu(root, tearoff=0)


m1 = Menu(New_menu)
m1.add_command(label= "Save",command= myfunc())
m1.add_command(label= "Save as",command= myfunc())
m1.add_separator()
m1.add_command(label= "Print",command= myfunc())
m1.add_command(label= "New File",command= myfunc())
m2 = Menu(New_menu)
m2.add_command(label= "Save",command= myfunc())
m2.add_command(label= "Save as",command= myfunc())
m2.add_separator()
m2.add_command(label= "Print",command= myfunc())
m2.add_command(label= "New File",command= myfunc())

New_menu.add_cascade(label= "File", menu= m1)
New_menu.add_cascade(label= "Edit", menu= m2)
root.config(menu = New_menu)
# gui logic
root.mainloop()