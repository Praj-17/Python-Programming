def searchInsert( nums: list[int], target: int) -> int:
    high = len(nums) -1
    low = 0
    mid = 0
    while low <= high:
        mid = (high + low)//2
        print(mid)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid+1 
        elif target < nums[mid]:
            high = mid - 1
        if mid == 0: return 1
        elif low > high:
            return mid
print(searchInsert([1,3,5,6], 2))
    
        