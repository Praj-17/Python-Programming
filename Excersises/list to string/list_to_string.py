n = int(input())
records = []
for i in range(n):
        name = (input())
        score = (float(input()))
        records.append([name, score ])

records.sort(key = lambda x:x[1])

min = records[0][1]

a = -23423
b = -3235
for i in records:
    if(i[1:2][0] == min):pass
    elif(i[1:2][0]>min):
        a = i[1:2][0]
        break
def listToString(s): 
    # initialize an empty string
    str1 = "" 
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    # return string  
        return str1
l =[]
for i in records:
    if(i[1:2][0] == a ): l.append(i)
l.sort() 
for i in l:
    str1 = i[0:1]
    str(str1)
    print(listToString(str1))
    
