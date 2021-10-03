size = int(input("Pls input the size of the list:- "))
l = []
i = 0
while i<size:
    inp = int(input("Pls input the list one by one:- "))
    l.append(inp)
    i = i+1
print(f"The given list is\n {l} ")
rev1 = l[:]
rev1.reverse()
print(f"The reverse of the list by built method is\n {rev1}")
rev2 = l[:]
revf = rev2[::-1]
print(f"The reverse of list by slicing method is:-\n {revf}", )
rev3 = l[:]
for i in range(len(rev3)//2 ):
    rev3[i], rev3[len(rev3)-i-1] = rev3[len(rev3)-i-1], rev3[i] 
print(f"The reverse of the list by swapping method is\n {rev3}")

if rev1 == revf == rev3:
    print("All the reverses are equal ")





