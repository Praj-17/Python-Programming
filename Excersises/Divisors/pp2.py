"""
Harry and the apples
"""
def Divisor(mn, mx , n):
    for i in range(mn, mx+1):
        if n % i == 0:
            print(f"{i} is a divisor of {n}")
            
        elif n%i != 0:   
            print(f"{i} is not a divisor of {n}") 
n = int(input(" pls input the total number of apples harry has:-  "))
mn = int(input("pls input the number of minimum apples to be distributed") )
mx = int(input(" pls input the maximum number ofa pples to be distrubuted"))


if mn == mx:
    print("This is not a valid range")
else:
    Divisor(mn, mx, n)