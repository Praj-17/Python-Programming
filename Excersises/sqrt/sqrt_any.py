def mySqrt(x: int) -> int:
        high= x 
        low = 0
        ans = 0
        if x == 0:
            return 0
        elif x == 1:
            return 1
        while low<=high:
            mid = (low+high)//2
            if mid*mid == x:
                ans =  mid
                return ans
            if mid*mid < x:
                low =  mid +1
                ans = mid
            else:
                high = mid - 1
        return ans

print(mySqrt(4))
            
        