def fibonacci(n):
    if n == 1:return 0
    elif n ==2: return 1
    else: 
        a = fibonacci(n-1)+ fibonacci(n-2)
        return a
print(fibonacci(6))