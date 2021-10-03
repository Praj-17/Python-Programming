#GCD CALCULATION
import time
initial = time.time()
def G_C_D(n1,n2):
    if n1>n2: greater = n1; lesser = n2
    else :greater = n2; lesser = n1
    s1 = set()
    s2 = set()
    for i in range(1,n1+1): 
        if n1%i == 0 : s1.add(i)
    for j in range(1,n2+1): 
        if n2%j == 0 : s2.add(j)
    print(f"the list of divisors of {greater} is ", s1)    
    print(f"the list of divisors of {lesser} is ", s2)    
    s3 = s1.intersection(s2)
    print("THE GCD OF THE GIVEN NUMBERS IS",max(s3))
G_C_D(493, 899)