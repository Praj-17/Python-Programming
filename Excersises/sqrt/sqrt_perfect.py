def IsPerfect(x:int) -> bool:
    divisors = []
    dividends = []
    if x == 0:
        return True
    elif x == 1:
        return True
    for i in range(2,x//2 +1):
        if x%i == 0:
            divisors.append(i)
            dividends.append(x//i)
    if len(divisors) ==1: return True
    if len(divisors) == len(dividends) !=0:
        if divisors[len(divisors)//2] == dividends[len(dividends)//2]: return True
    else: return False
def mySqrt( x: int) -> int:
    divisors = []
    dividends = []
    if x == 0:
        return 0
    elif x == 1:
        return 1
    for i in range(2,x//2 +1):
        if x%i == 0:
            divisors.append(i)
            dividends.append(x//i)
    if len(divisors) == len(dividends) !=0:
        if divisors[len(divisors)//2] == dividends[len(dividends)//2]: return dividends[len(divisors)//2]
    elif len(divisors) ==1:
        return divisors[0]
    
    #Else : Going for binary search
    high= x 
    low = 0
    ans = 0
    while low<=high:
            mid = (low+high)//2
            if mid*mid == x:
                ans =  mid
            if mid*mid < x:
                low =  mid +1
                ans = mid
            else:
                high = mid - 1
    return ans
    
print(mySqrt(2147395599))
       
    