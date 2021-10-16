x = int(input()) #1
y = int(input()) #1
z = int(input()) #1 
n = int(input()) #2
l1 =[i for i in range(x+1)]  #0,1
l2 =[i for i in range(y+1)]  # 0,1 
l3 =[i for i in range(z+1)]  # 0,1

permut = [[i, j, k] for i in l1 
                 for j in l2
                 for k in l3 ]
print(permut)