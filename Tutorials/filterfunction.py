#this function takes a function and a list as an argument and the filter the list according to the function
seq = [0,1,2,3,4,5,6,7,9,10]
result = list(filter( lambda x: x%2 ==0,seq))#Remember to put the 'list' word if u want a list or anyother data structure type
print ("odd numbers list :", result)
result = list(filter( lambda x: x%2 ==1,seq))
print ("Even numbers list :", result)
print("-------------------")

def square(a): return a*a
def cube(a):return a*a*a

func = [square, cube]
for i in range (10):
    val = list(map(lambda x: x(i), func))
    print(val)
#TAKEAWAY = you can also make a list of

    