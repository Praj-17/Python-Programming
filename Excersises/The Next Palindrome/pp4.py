#The Next Palindrome
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


for i in strings:
    oi = i
    j =int(i)
    if isPalindrome(i) == True:
        print(f"The given number {i} is already a palindrome!")
    else :
        while(isPalindrome(i) == False):
            
         
            j+=1
            i = str(j)
    print(f"The next palindrome of {oi} is {j} ")   
