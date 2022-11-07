nums = [-2,1,-3,4,-1,2,1,-5,4]
cur_max, max_till_now = 0, float('-inf')
for c in nums:
    cur_max = max(c, cur_max + c)
    max_till_now = max(max_till_now, cur_max)
print(max_till_now)