#Fibonacci series
# 0,1 ,1,2,3, 5,8
def fibonacci(n):
    if n < 0: print("Incorrect input")
    elif n == 0 : return 0
    else: 
        a,b=0,1
        for i in range(1, n):
            c = a+b
            a =b
            b = c
            
    return(b)
print("Pls enter the number upto which u want to calculate your fibonacci series",)
n = int(input())
for i in range(n): print(fibonacci(i), end = ' ')


         
    

    
        
   
    



    




