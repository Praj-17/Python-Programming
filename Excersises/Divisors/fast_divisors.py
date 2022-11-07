def get_divisors(n):
    divisors = [1,]
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            divisors.append(i)
            t = n//i
            if t != i:
                divisors.append(n//i)
    return divisors

print(get_divisors(100))
        