
n1,n2 = (input().split())
ans = 1
l1  = [1]
l2  = [1]
greater = 0
lesser = 0
if(n1>n2):   
    greater = n1
    lesser = n2
elif(n2> n1): 
    greater = n2 
    lesser = n1 
#Bade wale ke sirf dusre wale tak
#Chhote wale ke saare
#let n1 bada hai
# n1 = 10, n2 = 15
for i in range (2,(int(lesser)+1)//2): 
    if int(lesser)%i == 0: l1.append(i) 
l1.append(int(lesser))
for i in range (2,(int(lesser)+1)//2):
    if int(greater)%i == 0: l2.append(i)
for i in l1:
    if i in l2: ans +=1
print(ans)