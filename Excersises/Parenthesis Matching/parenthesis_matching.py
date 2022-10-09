def isValid(s: str) -> bool:
    stack = []
    opening = ('(', '{', '[')
    closing = (')', '}', ']')
    if len(s) %2 == 1:
        return False 
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            #check weater recent input is its opposite
            
            if (len(stack)>0) and (stack[-1] == opening[closing.index(char)]):
                stack.pop()
            else:
                return False
            
    if len(stack) == 0:
        return True
    else: return False
print(isValid("([}}])"))
