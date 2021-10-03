#This is a program used to learn importing of MODULES  

import math
print(math.sin(67))
print(math.sqrt(36))
print(math.degrees(math.pi))
print(math.pi)
print(math.sin(math.radians(30)))
print("------------------")
#import using as
import math as m
print(m.sin(m.radians(30)))
print(m.log(10))
print(m.e)
print("------------------")
#Using From import: this helps u any specific atribue from a module instaead of importing it as whole\
from math import sin, log, pi
print(sin(30))
print(log(23))
print(pi)
print("------------------")
#CREATING A MODULE
#you only have to create a normal python file and then import it here
import functions  #ITS GIVING SOME STUPID ERROR BEACAUSE OF MY INCORRECT FILE SAVINGS
a = 2
