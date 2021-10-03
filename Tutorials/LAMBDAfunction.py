"""A lambda function is an ANONYMOUS function , it has very less bakchodi and can be used to define smaller fucntions like sqaures, addition and all smaller one lined functions"""
x = lambda a:a*a
print(x(5))
minus = lambda x,y: x-y
add = lambda x,y: x+y
print(add(9,4))
a = [[1,14],[2,4], [3,25]]
def a_first(a):
    return a[1]
a.sort(key = a_first)
print(a)
