# THIS PROGRAM IS BASED ON BROADCASTING
"""
COMPATIBILITY of ARRAYS - 2 arrays are said to be compatible if they have the same size and dimensions and if the ith element of the first element is greater than or equal to the ith element in the second array for all i in arrays and vis versa
#3 rules of broadcasting stretching

 Rule 1: If the two arrays differ in their number of dimensions, the shape of the one 
with fewer dimensions is padded with ones on its leading (left) side.
 Rule 2: If the shape of the two arrays does not match in any dimension, the array with 
shape equal to 1 in that dimension is stretched to match the other shape.
 Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is 
raised.
"""
import numpy as np
from numpy.core.fromnumeric import reshape
#RULE 1 
a = np.ones((2,3)) # this functions is used to create an array 2 dimensional array 3 one D arrays and 1 as their elements
print(a)
b = np.arange(3)  #this function is used to create an array from o to 3 as elements in one dimension
print(b)
print(type(a))
print(type(b))
C = a+b
print(C)
print("----------------")
#RULE 2
a = [[0],[1],[2]]
print(a)
b = np.arange(3)
print(b)
c = a+b
print(c)
print("----------------")
#RULE 3
#When the 2 arrays are not compatible
a=np.ones((3,2))
print(a)
b=np.arange(3)
print(b)
#C=a+b 
#print(C)




