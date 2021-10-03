l1 = ["1","2","3","4","5"]
i = 1
for item in l1:
    if i %2 is not 0:
        print(f"Jarvis please buy ", {item})
    i = i+1
for index, item in enumerate(l1):
    if index%2 ==0:
        print(f"Jarvis please buy ", {item}) 
        
    