from tkinter import *
import pandas as pd
root = Tk()
root.geometry("655x444")

Label(root, text = "Welcome to Praj-Travels", font ="comicsansms 13 bold", padx= 4, pady=15).grid(row =1, column=3) 

#Creating the labels
name = Label(root, text = "Name")
phone =Label(root, text= "phone")
address =Label(root, text= "address")
email =Label(root, text= "Email")
gender =Label(root, text= "Gender")
payment_mode = Label(root, text="payment mode")
foodServiceValue = IntVar()
#placing them in the box using grid
name.grid(row =2 , column=2)
phone.grid(row =3 , column=2)
address.grid(row =4 , column=2)
email.grid(row =5 , column=2)
gender.grid(row =6 , column=2)
payment_mode.grid(row = 7,column=2 )

#Definig the desired datatypes

namevalue = StringVar()
phonevalue = StringVar()
addressvalue = StringVar()
emailvalue = StringVar()
gendervalue = StringVar()
paymentvalue = StringVar()


#Creating the entries
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
addressentry = Entry(root, textvariable=addressvalue)
emailentry = Entry(root, textvariable=emailvalue)
genderentry = Entry(root, textvariable=gendervalue)
paymententry = Entry(root, textvariable=paymentvalue)





#Taking the required input
nameentry.grid(row = 2, column = 3)
phoneentry.grid(row = 3, column = 3)
addressentry.grid(row = 4, column = 3)
emailentry.grid(row = 5, column = 3)
genderentry.grid(row = 6, column = 3)
paymententry.grid(row = 7, column = 3)

#Checkbox
foodservice = Checkbutton(text="want to prebook your meals?", variable=foodServiceValue).grid(row= 8, column=3)

#submit button
def getvals():
    print("submitted")
    
        
Button(text= "Submit", command=getvals).grid(row=9, column= 3)
# gui logic
root.mainloop()