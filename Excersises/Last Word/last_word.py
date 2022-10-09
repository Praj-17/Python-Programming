def lengthOfLastWord(s: str) -> int:
    space_count = 0
    for i in reversed(range(len(s))):
        if s[i] != ' ':
            break
        else: 
            space_count += 1
    if space_count>0:
        s = s[:-space_count]

    return len(s.split(' ')[-1])   

print(lengthOfLastWord("Hello World"))
        
        