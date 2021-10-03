s = set()
print(type(s))
l = [1,2,3,4]
s_from_list = set(l)
print(type(s_from_list))
print(s_from_list)
s.add(6)
s.add(1)
s.add(1)
print(s)
s1 = s.union({1,2,3})
print(s,s1)
print(len(s1))


