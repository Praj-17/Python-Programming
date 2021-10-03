# import random
# char_list = ['a','e','i','o','u']
# random.shuffle(char_list)
# print(''.join(char_list))

l = [i for i in range(100)]
while (len(l)>0):
    for i in l:
        if i%3 == 0: l.remove(l[i])
        print(l)
        
