#This program prints the table of a number
n = int(input("pls input a positive integer  "))
def table(n):
    i = 0
    while(i<=10):
        print(n,"*",i,"=" , n*i)
        i+=1

object = table(n)
print(object)
        
        