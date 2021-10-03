from typing import ClassVar


class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self) -> None:
        self.var1 = "I am in class A constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "SPECIAL"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self) -> None:
        super().__init__()
        self.var1 = "I am in class B constructor"
        self.classvar1 = "Instance var in class B"
    
a = A()
b = B()
print(b.classvar1)
print(b.special, b.var1, b.classvar1)