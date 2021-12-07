from tkinter import *

root = Tk()
root.geometry("444x233")
root.title("MY GUI")
# _________Important label items_________
"""
text = adds the text
bd = background
fg = foreground ---Font color
font = sets the font ----- font =("comicsansas", 21, "bold") or "comicsansas 21 bold"
padx = x_padding
pady = y_padding
borderwidth = border's width
relief = border styling- Sunken, Raised, Groove, RIDGE
"""
#___________implementation_______
title_label = Label(text = "READY" , bg = "green", fg= "white", padx= 80, pady= 30 , font =("comicsansas", 21, "bold"), borderwidth= 10, relief= SUNKEN )
#______________Pack options__________
"""
anchor = "ne" // northeast it determins where exactly to place your label
side = top, bottom, left, right
fill- when you your label to expand when you expand the window we use fill
padx,pady = padding


"""
title_label.pack(anchor= "s", side = "bottom", fill= X )

  



# ________________
root.mainloop()