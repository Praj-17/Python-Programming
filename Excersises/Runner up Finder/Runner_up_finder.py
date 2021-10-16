n = int(input())
arr = map(int, input().split())
l = list(arr)
l.sort(reverse =True)
print(l)
max = l[0]
print(max)
for i in l:
       if(i != max ):
           max = i
           print(i)
           break
           
           
            
        