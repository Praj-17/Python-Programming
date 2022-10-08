def romanToInt(s: str) -> int:
    s ="MCMXCIV"
    ans = 1000 + 1000 -100 + 100 - 10 +  5 -1
    print("ans", ans)
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
        print("id", id)
        print('integer' ,integer)
        if id==0:
            if r[s[0]]>=r[s[1]]:
                print('adding1', r[s[id]])
                integer+= r[s[id]]
            else:
                print("Continued")
                continue
        else:
            if r[s[id-1]]<r[s[id]]:
                    print("adding2", r[s[id]] - r[s[id-1]])
                    integer = integer + (r[s[id]] - r[s[id-1]])
            elif r[s[id-1]]>=r[s[id]] and :
                print('adding4', r[s[id]])
                integer+= r[s[id]]
    return integer
print(romanToInt('LVIII'))