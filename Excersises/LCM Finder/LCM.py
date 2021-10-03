def LCM (x,y):
    if x>y:
        greater = x
    else: greater = y
    while (True):
        if greater%x ==0 and greater%y ==0:
            break
        greater +=1
    return greater

num1 = int(input("Input First Number"))
num2= int(input("Input Second Number"))
print("The LCM of given 2 number is:",LCM(num1, num2))