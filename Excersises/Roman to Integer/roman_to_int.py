def romanToInt(s: str) -> int:
    s ="CMLII"
    ans = 900 + 50 + 1 + 1
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
    for id, char in enumerate(s):
        print("id", id)
        print('integer' ,integer)
        if id == 0 and r[s[0]]>=r[s[1]]:
            print('adding1', r[char])
            integer+= r[char]
            continue
        # if id == 0 and r[s[0]]<r[s[1]]:
        #     print('adding 5',(r[s[1]] - r[s[0]]) )
        #     integer = integer + (r[s[1]] - r[s[0]])
        #     id+=1
        #     continue
        else:
            if id==0:
                continue
            if r[s[id-1]]<r[s[id]]:
                print('id',id)
                print("adding2", r[s[id]] - r[s[id-1]])
                integer = integer + (r[s[id]] - r[s[id-1]])
                continue
            if id == len(s)-1 :
                print('adding3', r[char])
                integer+= r[char]
                continue   
            if r[s[id]]<r[s[id+1]]:
                continue
            else:
                print("id",id)
                print('adding4', r[s[id]])
                integer+= r[s[id]]
        print("End of ", id)
        return integer
print(romanToInt('LVIII'))
        