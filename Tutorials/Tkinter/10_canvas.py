from tkinter import *
root = Tk()
root.title("Canvas")

canvas_width  = 800
canvas_height = 400


root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

#This line goes from (x1 , y1) to (x2,y2)
can_widget.create_line(0,0,800,400, fill="green")
can_widget.create_line(0,400,800,0, fill="red")

#to create a reactangle specify the parameters in this order
#co-ordinates of top left corner to the cordinates of bottom right corner
# can_widget.create_rectangle(3,5,700,300, fill= "blue")

can_widget.create_text(200, 200,text = "python")

can_widget.create_oval(100,400, 400,100)
 


# gui logic
root.mainloop()