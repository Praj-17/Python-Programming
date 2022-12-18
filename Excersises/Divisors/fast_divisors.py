def get_divisors(n):
    divisors = set(1,n)
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            divisors.add(i)
            t = n//i
            if t != i:
                divisors.add(n//i)
    return divisors

print(get_divisors(100))
        