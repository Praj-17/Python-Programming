# def function1():
#     print("Subscribe Now")
# func2 = function1
# del function1
# func2()
def dec1(func1):
    def nowexecute():
        print("executing now")
        func1()
        print("executed")
    return(nowexecute)
@dec1
def prajwal():
    print("prajwal is a good boy")
prajwal = dec1(prajwal)
prajwal()
