#This program prints the sequence 
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 
print("print the last number")
n = int((input()))
for i in range(int(n+1)): print (str(i)*i, end='')
