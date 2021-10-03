#the program says weather it is not a prime number and prints nothing if it is prime

print("pls insert a number")
n = int(input())
for i in range(2, n):
    if (n%i !=0): continue
    else:print("it is not a prime number")
    break


