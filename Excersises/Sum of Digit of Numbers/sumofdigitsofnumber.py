#Sum of digits of numbers of a given number
print("Pls input your number")
n = int(input())
last_digit = 0
sum = 0
while n>0:
    last_digit = n%10
    n = n/10
    sum = sum +int(last_digit)

print(sum)
    
