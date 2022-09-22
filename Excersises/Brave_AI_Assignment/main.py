#Task-1
#One liner code to remove capital and digits 
import re
input_list = ['1aGpple', '2Uboy', '3cat4', '5li3on3']
output = list(map(lambda text :re.sub(r'[^a-z ]+', '', text), input_list))
print(output)

#Task-2
# Question 2:  A Girl meets a lion and unicorn in the forest. The lion lies every Tuesday, Wednesday, and Thursday and on the other days he speaks the truth. The unicorn lies on Fridays, Saturdays, and Sundays and the other days of the week he speaks the truth. “Yesterday I was lying,” the lion told the girl. “So was I,” said the unicorn. What day is it?

# --> Thursday

#Task-3
# Question3: Write a python code to Split the input number such that the product of the digit on the right is equal to the product of the digit on the left.   Output the split position, if split is not possible then return -1, if multiple splits are possible then return the least split position.
# Algorithm: 
#     Let's say there are n digits in a number
#     at first iteration i = 0, left part = 0, right  = 1 to n-1
#     at second iteration i = 1 left part = 0,1 right = 2 to n-1
#     at kth iteration   index = i left part = 0 to k, right = k+1 to n-1
#     left_product = 0 to k
#     right_product = k+1 to n
#     if left_product == right_product
#         return i:
        
s = "2011210"
m = []
for i in range(len(s)):
    l = s[:i+1]
    r = s[i+1:]
    # print(l,r)
    p1 = 1
    for i1 in l:
        p1*=int(i1)

    p2 = 1
    for i2 in r:
        p2*=int(i2)
    # print(p1,p2)
    if p1 == p2:
        m.append(i+1)
print(min(m))