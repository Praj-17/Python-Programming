#prime numbers in a range
n1 = int(input("Enter first number  "))
n2 = int(input("Enter secondnumber  "))
i =0 
j = 0
def Isprime(j):
    for i in range(2,j):  
        if j%i == 0:
            return False
    else: return True
        
for j in range(n1,n2):
    if Isprime(j) == True:print(j," ", end= '')

       
    

 
