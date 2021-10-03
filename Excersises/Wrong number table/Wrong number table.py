#Rohan Das Is A Fraud
import random
def Rohansmultiplication(number):
    wrong = random.randint(0,9)
    table = [i*number for i in range (1,11)]
    table[wrong] = table[wrong] + random.randint(0,10)
    return table
def iscorrect(table, number):
    for i in range (1,11):
        if table[i-1] != i*number:
              return i -1
    return None
number = int(input("Pls input a number:- \n"))
mytable = Rohansmultiplication(number)
print(mytable)
wrongindex = iscorrect(mytable, number) 
print(f" The table is wrong at the index {wrongindex}")