#list comprehensions
ls = [i for i in range(100) if i%3 == 0]
print(ls)
#dictionary comprehensions
dict1 = {i: f" Item {i}" for i in range(100) if i %3 ==0}
dict1 = {value:key for key, value in dict1.items()}
print(dict1)
# set comprehensions
dresses = {dress for dress in ["dress1", "dress2"
                               "dress1", "dress2"
                               "dress1", "dress2"
                               "dress1", "dress2"]}
print(dresses)
#generaotrs
evens = (i for i in range(100) if i%2 ==0 )
for i in evens: print(i, end = " ")