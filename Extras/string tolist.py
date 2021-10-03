s = '''
1. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other. Go to the editor
Click me to see the sample solution

2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once. Go to the editor
Click me to see the sample solution

3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
Click me to see the sample solution

4. Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers. Go to the editor
Click me to see the sample solution

5. Write a Python program to create the combinations of 3 digit combo. Go to the editor
Click me to see the sample solution
'''
w = s.split(" ")
print(w)
l1 = [w.count(i) for i in w ] 

print(l1)
