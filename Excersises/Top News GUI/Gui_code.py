from tkinter import *
from PIL import Image , ImageTk
root = Tk()
root.title("Aap ka Apna Akhbaar")
root.geometry("1000x600")
texts = []
photos = []

def every_100(text):
    final_text = ""
    for i in range(0,len(text)):
        final_text+= text[i]
        if i%100 == 0 and 1!=0:
            final_text += "\n"
    return final_text
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))
        image = Image.open(f"{i+1}.png")
        #TODO: resize these images 
        
        photos.append(ImageTk.PhotoImage(image))
f0 = Frame(root, width = 800, height = 70)
Label(f0,text = "The Praj News", font="lucida 33 bold italic").pack()
Label(f0,text = "18th Nov 2021", font="lucida 20 bold italic").pack()
f0.pack()
f1 = Frame(root, width = 900, height = 200)
Label(f1, text= texts[0], padx=22, pady=22).pack(side="left")
Label(f1, image= photos[0], anchor = "e").pack(side="left")
f1.pack(anchor="w")
f1.pack()

f2 = Frame(root, width = 900, height = 200)
Label(f2, text= texts[1], padx=22, pady=22).pack(side="right")
Label(f2, image= photos[1], anchor = "e").pack(side="left")
f2.pack(anchor="w")
f2.pack()

f3 = Frame(root, width = 900, height = 200)
Label(f3, text= texts[2], padx=22, pady=22).pack(side="left")
Label(f3, image= photos[2], anchor = "e").pack(side="left")
f3.pack(anchor="w")
f3.pack()
root.mainloop()