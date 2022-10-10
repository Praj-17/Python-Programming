
#using Recurssion
def fibR( n: int) -> int:
    if n ==0 or n == 1: return n
    return fibR(n-1) + fibR(n-2)

#Using DP
results = [-1 for i in range(31)]
def fibDP( n: int) -> int:
    if n ==0 or n == 1: return n
    if results[n] != -1: return results[n]
    results[n] =  fibDP(n-1) + fibDP(n-2)
    return results[n]

print(fibDP(25))
