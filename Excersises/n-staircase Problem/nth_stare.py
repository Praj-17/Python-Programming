

#Using Recurssion w/o DP

def climbStairsRecursion(n: int) -> int:
    #The recurrence relation in problems
    # f(n) = f(n-1) + f(n-2)
    if n == 1 or n ==2: return n
    else: return climbStairsRecursion(n-1) + climbStairsRecursion(n-2)

results = [-1 for i in range(46)] #Hash Table
def ClimbStairsDP(n: int) -> int:
    if n == 1 or n ==2: return n
    if results[n]!=-1: return results[n]
    
    results[n] =  ClimbStairsDP(n-1) + ClimbStairsDP(n-2)
    return results[n]


# print(ClimbStairsDP(25))
print(climbStairsRecursion(25))