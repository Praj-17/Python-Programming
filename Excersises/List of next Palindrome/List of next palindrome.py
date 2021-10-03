#The Next Palindrome Less than 10
def isPalindrome(s):
    rev = s[::-1]
    if str(s) == str(rev):
        return True
    else: return False
        
    
    
n = int(input("Pls input the number of test cases:- "))
strings = []

for i in range(n):
    str1 = input(f"Pls input the {n} numbers one by one:- ")
    strings.append(str1)
print(f"The given list of test cases is:-\n {strings}")
Palindromes = []

for i in strings:
    j =int(i)
    if j>=10:
        if isPalindrome(i) == True:
            print(f"The given number {i} is already a palindrome!")
        else :
            while(isPalindrome(i) == False):
             j+=1
             i = str(j)
        Palindromes.append(j)
    else: print(f"The number {j} is less than 10. So Palindrome can not be computed")  
print(f"The list of the Palindromes thus formed is\n {Palindromes} ")
