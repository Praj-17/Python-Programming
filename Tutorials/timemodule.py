import time 
initial = time.time()
for i in range (1000):
    print("this is prajwal's dekstop")
print("for loop ran in ", time.time()-initial)
initial2 = time.time()
p = 0
while (p<1000):
    print("this is prajwal's dekstop")
    p = p+1
print("while loop ran in ", time.time()-initial2)
localtime = time.asctime(time.localtime(time.time()))
print(localtime)