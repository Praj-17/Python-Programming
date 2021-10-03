#pattern printing
print("Enter the number of lines")
n = int(input())
print("pls input 0 for descending pattern or 1 for ascending")
b = bool(int(input()))



if( b == 1 ) :
    for i in range(n):
        print("*"*(i+1))
elif(b == 0):
    for i in range(n):
        print("*"*(n-i))
        
        
         
        

       

    

   


    

     


