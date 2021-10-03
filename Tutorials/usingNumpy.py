import numpy as n
from numpy.core.numeric import convolve
from numpy.lib.function_base import append

#ONE DIMENSIONAL ARRAY
a = n.array([1,2,3,4,5,6,7,8,9,0])
print(a)
print(n.sort(a))
print(type(a))
print(len(a))
for i in a :print(i,"", end = '')
("3")
print(a)
b = n.append(a,11)
print(b)
c = n.delete(b,5)
print(a)
print(b)
print(c)
print(c[9])
print(b[9]+b[2])
print(a/4)
print("----------------------")
#2 DIMENSIONAL ARRAY
arr = n.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,1])
print(arr[1,4])
print("----------------------")
#3 DIMENSIONAL ARRAY
Arr = n.array([[[1,2,3],[4,5,6]] , [[7,8,9],[10,11,12]]])
print(Arr[0,1,1])
print("----------------------")
#4 DIMENSIONAL ARRAY
ARR = n.array([[[[1,2,3],[4,5,6]] , [[7,8,9],[10,11,12]]],      [[[21,22,23],[24,25,26]] , [[27,28,29],[210,211,212]]]])
print(ARR[1,1,0,2])
#NEGATIVE INDEXING
#neGATIVE INDEXING OF COURSE STARTS FROM -1 RATHER THAN 0
print(ARR[-1,-1,0,-2])
print("----------------------")
#List Vs arrays
"""
Advantages of arrays over lists
1. Less Memory
2. Fast
3. Convenient
Data scientist use Array more than list
"""
#You can ignore this code for now
import time
import sys
s = range(1000)
print(sys.getsizeof(s)*len(s)) #output = 48k bits
d = n.arange(1000)
print(d.size*d.itemsize)#output = 4k bits
#You can see how the memory used for arrays is less
print("----------------------")
#OPERATIONS IN NUMPY
#1. ndim
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(arr.ndim)
print(Arr.ndim)
print(ARR.ndim)
print("----------------------")
#2. itemsize
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)
print(Arr.itemsize)
print(ARR.itemsize)
print(arr.itemsize) # it will print all 4 beacuse in all arrays we have put integers
print("----------------------")
#3. dtype, size, shape
#this function prints the data type and the number of bits occupied
print(a.dtype)
print(b.dtype)
print(c.dtype)
print(arr.dtype)
print(Arr.dtype)
print(a.size)
print(a.shape)
print("----------------------")
#4. Reshape for 2D arrays
arr = n.array([[1,2,3,4,5],[6,7,8,9,10]])
A = arr.reshape(5,2)
print(A)
A = arr.reshape(1,10)
print(A)
print("----------------------")
#5. Slicing for 2D arrays
print(arr[0:,2])
"""
Here 0 means rows
: says 0 is sacting as rows
 and 2 represents its the 2nd row
"""
arr = n.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr[0:2,3])
print(arr[0:2,3])
print("----------------------")
#linspace #kuch nai bore hai
p = n.linspace(1,3,10)
print(p)
print("----------------------")
# max/min/sum
print(a.max())
print(a.min())
print(a.sum())
print("----------------------")
#axis usage
arr = n.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr.sum(axis = 0))#adds along coloumns
print(arr.sum(axis = 1))#adds along rows
print("----------------------")
#Square root and Standard deviation
print(n.sqrt(arr))
print(n.std(arr))
print("----------------------")
#Arithimatic operations on arrays
ARRAY1 = n.array([[1,2],[3,4]])
ARRAY2 = n.array([[1,2],[3,4]])
print(ARRAY1+ARRAY2)
print(ARRAY1-ARRAY2)
print(ARRAY1*ARRAY2)
print(ARRAY1/ARRAY2)
print("----------------------")
#VERTICAL AND HORIZONTAL STACKING
print(n.vstack((ARRAY1,ARRAY2)))
print(n.hstack((ARRAY1,ARRAY2)))
print("----------------------")
#PYTHON SPECIAL FUNCTIONS USING NUMPY
# 1. sin function
import math as m
in_array = [0,m.pi/2,n.pi/3,n.pi]
print("Imput array:\n", in_array)
sin_values = n.sin(in_array)
print("\nSine values: \n", sin_values)
print(m.pi)
print(n.pi)
print(type(m.pi))
print(type(n.pi))
print("----------------------")
#2. cos function
in_array = [0,m.pi/2,n.pi/3,n.pi]
print("Input array:\n", in_array)

cos_values = n.cos(in_array)
print("\ncosine values: \n", cos_values)
print("----------------------")
#FUNCTIONS FOR ROUNDING
#1. Around function
in_array= [.5,1.5,2.5,3.5,4.5,10.1]
print("Input array:\n", in_array)

round_off_values = n.around(in_array)
print("the rounded values are:\n", round_off_values)

in_array= [.5153,1.3456, 3.4535,4.115351]
print("Input array:\n", in_array)

round_off_values = n.around(in_array,2)
print("the rounded values are:\n", round_off_values)
print("----------------------")

#EXPONENTS AND LOGARITMIC FUNCTIONS
#exp() function  - it will do e to the power x
in_array = [1,3,5]
print("Input array:\n", in_array)

exp_value = n.exp(in_array)
print("the exp array is =\n ", exp_value)
print("----------------------")

#logarithmic functions
in_array = [1,3,5]
print("Input array:\n", in_array)

log_value = n.log(in_array)
print("the log array is =\n ", log_value)
print(m.log(2**8))
print(m.log(2))
print(m.log(2)*8)
print(n.around(m.log(2)*8,2))
print("----------------------")
# Arithmetic functions
#1. Reciprocal
in_array = [1.0,3.0,5.0]
print("Input array:\n", in_array)

recipo_value = n.reciprocal(in_array)
print(recipo_value)
print(n.reciprocal(2.0))
print("----------------------")

#convolve function
arr1 = [1,2,3,4]
print(n.convolve(arr1,3)) 
print(n.multiply(arr1,3))
print(n.absolute(arr1))
print("----------------------")






















