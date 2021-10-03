# Input  a number from user and then Reverse it

print("Pls input a positive integer")
n = int(input())
print("The number in reverse is: ")
while(n>0) :
    last_digit= int(n%10)
    n = n//10
    print(  last_digit, end = ' ')
    