# F strings
me = "prajwal"
import math
a1 = 3 
# #a = "this is %s %s  "%(me, a1)
# a = "this is {1} {0} "
# b = a.format(me, a1)
# print(b)
# ACTUAL F STRINGS
a = f"this is {me} {3} {math.cos(65)}"
print(a)