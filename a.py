l = []
for  _ in range(3):
    a = input()
    l.append(a)
print(l)
count = 0
for i in range(len(l)):
    for j  in range(len(l[i])):
        # print(l[i][j] )
        if l[i][j] == '7':
            count +=1
            # print(count)
            
    if(count>0): print("yes")
    else: print("no")


        
    
    
        
    
        