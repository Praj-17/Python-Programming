# def removeDuplicates( nums: list[int]) -> int:
#     i = 0
#     for j in range(1, len(nums)): # 1 to 3   (1,2,3)
#         if (nums[i] != nums[j]): 
#             i += 1
#             nums[i] = nums[j]
#     i +=1
#     return i


'''
take 2 pointers one is slow (i) and other is fast
 if nums[i] != nums[j] which means if numbers ith and j to len(nums) are not equal
 for bring them just before i 
 else:
 

'''

def removeDuplicates( nums: list[int]) -> int:
        i = 0 # slow pointer
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i +=1
                nums[i] = nums[j]
        i+=1
        print(nums, i)
        return i

removeDuplicates([1,1,1])