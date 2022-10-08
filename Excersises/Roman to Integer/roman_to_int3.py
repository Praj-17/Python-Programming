def romanToInt(s: str) -> int:
    # s ="LVIII"
    # ans = 1000 + 1000 -100 + 100 - 10 +  5 -1
    # print("ans", ans)
    r = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000}
    integer = 0
    for id in range(len(s)):
        if id == len(s)-1:
            integer += r[s[id]]
            break
        if r[s[id+1]] > r[s[id]]:
            integer -= r[s[id]]
        else: integer += r[s[id]]
    return integer
print(romanToInt('LVIII'))