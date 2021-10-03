# import sys
# print(sys.version)
# print("---------")
# print(sys.version_info)
# print("---------")
# import time
# localtime =time.asctime (time.localtime(time.time()))
# print(localtime)
# print("---------")
# name = "prajwal"; surname = "waykos"
# print(surname, name)
# print("---------")
# Values = input("input some comma separated numbers")
# list = Values.split()
# tuple = tuple(list)
# print('Tuple', tuple)
# print('list', list)

#7
# filename = input("input the Filename: ")
# f_extn = filename.split(".")
# print("the extension of the file is:  " + repr(f_extn[-1]))

#8
# print(abs.__doc__)
# #12
# # import calendar
# # y = int(input("input the year: "))
# # m= int(input("input the month: "))
# # print(calendar.month(y,m))
# #13
# print(""" a
#       a
#       a
#       a
#       a
#       """)
# #14
# from datetime import date
# f_date = date(2002,1,17)
# l_date = date(2002,3,17)
# delta = l_date-f_date
# print(delta)
#15 #16
# n = int(input("input ur number"))
# if(n in range(100, 1000)):print("number lies within 100 and 1000")
# elif(n in range(1000,2000)): print("number lies within 1000 to 2000")
# else:print("number not in range")
#19
# def new_string(str):
#   if len(str) >=2 and str[:2] =="is":
#     return str
#   return "Is" + str
# userstring = input("input ur string")
# print(new_string(userstring))
#20 
# def larger_string(str, n):
#   result = ''
#   for i in range(n):
#     result = result+ str
#   return result
  
# print(larger_string(' praj ',3))
# print(larger_string(' aish ',4))
# l = [1,2,3,4,4,6,6,4,5]
# print(l.count(4))
# def print_str(n, str):
#   if len(str)<2: print(str)
#   else: print(str[:2]*n)

# print_str(4, "prajwal")
# def is_vowel(char):
#   all_vowels = "aeiou"
#   return char in all_vowels
# print(is_vowel('c'))
# print(is_vowel('p'))
# print(is_vowel('a'))
# print(is_vowel('s'))
# print(is_vowel('b'))
# import functools 
# def histogram(list):
#   for i in list : print(' @ '*i)
    
# def histogram(lis):
#   a =list(map(lambda i: '@'*i, lis))
#   print(a,"\n")
           
  
# l1 = [1,2,3,4,5,6]
# histogram(l1)

# def add_numbers(a,b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         return "Inputs must be integres!"
#     return a+b
# print(add_numbers(10,20))
# print(add_numbers(10.2,20.3))
# import os.path
# print(os.path.isfile('main.txt'))
# print(os.path.isfile('main.py'))
# print(os.path.isfile('strings.py'))
# print(os.path.isfile('text.txt'))
# print(os.path.isfile('Module 2'))
# print(os.path.isfile('a.py'))
# print(os.path.isfile('MAIN1.py'))
# print(os.path.isfile('MAIN2.py'))

# import struct
# print(struct.calcsize("p") * 8)
# import os
# import platform
# print(os.name)
# print(platform.system())
# print(platform.release())
# import site
# print(site.getsitepackages())
# import time
# initial = time.time()
# num1, num2 = 13, 26
# l1, l2,l3 = [], [], []
# for i in range(1,num1+1):
#     a = num1 % i
#     if a==0:
#         l1.append(i)
# for j in range(1,num2+1):
#     b = num2 % j 
#     if b==0:
#         l2.append(j)
# for k in l1:
#     for m in l2:
#             if k==m:
#                 l3.append(k)
# print("The GCD of",num1,"and",num2,"is",max(l3))
# print(time.time()- initial)
# def absolute_file_path(path_fname):
#     import os
#     return os.path.abspath('path fname')
# print("Absolute path ", absolute_file_path("MAIN1,PY"))
# print("Absolute path ", absolute_file_path("a.py"))
# print("Absolute path ", absolute_file_path("Module 2"))
# import sys
# print()
# # print(sys.getrecursionlimit())
# # print()
# print()
# print(ord('a'))
# print(ord('b'))
# print(ord('c'))
# print(ord('d'))
# import os
# print(os.path.getsize("MAIN1.py"), "Bytes")
# l = [1,2,3]
# s = {1,2,3}
# t = (1,2,3)
# d = {1:2, 2:3}
# print(type(s))
# print(type(d))
# n = int(input("pls input a number  "))
# print(n*2)
print("\a My name is\n prajwal \a")