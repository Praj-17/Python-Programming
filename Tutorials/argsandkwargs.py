#ALWAYS RIGHT NORMAL, *ARGS, *KWARGS
# *args keyword is used to make no of arguments dynamic
def funargs(*args, **kwargs): # u can also change its name but args is conventional
    for item in args:
        print(item)
    for i,j in kwargs.items():
        print(f"{i} is a {j}")
 
list = ["harry","prajwal", "aishu", "saumya"]
    
kw = {"rohan" : "Monitor", "prajwal" : "chutiya"}
funargs(*list,**kw)  
    