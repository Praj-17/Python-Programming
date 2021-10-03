a = 5
b = 7
c = sum((a,b )) #built in fuction
print(c)

def function1(a, b):
    print("Hello you are in function 1", a+b)

def fucntion2(a, b):
    """ This is a function which will calculate average"""
    #the line above is a docstring and not a comment
    average = (a+b)/2
    print(average)
    return average
 

function1(5,7)
print(fucntion2.__doc__)
v =fucntion2(5 , 7)
print(v) 
