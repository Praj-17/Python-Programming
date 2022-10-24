#perfect number
def PerfectNumber(n):
        if n==1:
            return False
        sq=int(n**0.5)
        s=1
        for i in range(2,sq+1):
            if n%i==0:
                t=n//i
                print(i,t)
                s+=t+i
        if s==n:
            return True
        return False

print(PerfectNumber(28))