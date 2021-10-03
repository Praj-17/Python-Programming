class A:
    def met(self):
        print("this is a function from clas  A")
     
class B(A):
    def met(self):
        print("this is a function from clas B ")
    
class C(A):
    def met(self):
        print("this is a function from clas  C")

class D(B,C):
    def met(self):
        print("this is a function from clas  D")
    pass
a = A()
b = B()
c = C()
d = D()
d.met()