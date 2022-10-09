def removeDuplicates( nums: list[int]) -> int:
    counts = {}
    for i in nums:
        if i in counts.keys():
            nums = nums.remove(i)
        else:
            counts[i] = 0
removeDuplicates([1,1,2])
        
        