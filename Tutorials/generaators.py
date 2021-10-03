"""
Iterable - __iter__ or __getitem__
Iterator - __next__()
Iteration - 
Generators  are a type of Iterator
range is an generator
generators generate creates value on the way and not all in bulk
list is opposite of generator
"""
def gen(n):
    for i in range(n):
        return i 
    
gen(2)