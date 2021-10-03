#function ke andar function and then uske andar function
def print2(str1):
    
    print ("this is " + str1)
print2("prajwal")

def factoril1 (n):
    fac = 1
    for i in range (n):
        fac = fac*(i+1)
    return fac
print(factoril1(5))

def factorial2(n):
    if n ==1: return 1
    else: return(n* factoril1(n-1))
print(factorial2(5))
     
        


  