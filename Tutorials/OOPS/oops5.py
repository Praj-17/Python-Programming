"""
_varname = single underscore at start of name = protected
__varname = double underscore at start of name = private
"""

class Employee:
    no_of_leaves = 8
    _protect = 9
    __private = 99
    def __init__(self, aname, asalary, acompany):
        self.name = aname
        self.salary = asalary
        self.company = acompany
    
    
    def printdetails(self):
        return f"name is {self.name}, Salary is {self.salary}, company is {self.company}"
    @classmethod
    def from_ster(cls, string):
        Param = string.split("-")
        print(Param)
        # return cls(Param[0], Param[1],Param[2])
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("this is good" + string)
    
    
        
# print(Employee.__dict__)

prajwal = Employee("prajwal", 45, "google")
Aishu = Employee("Asihu", 45,"microsoft")
harry = Employee.from_ster("harry-48-apple")

print(harry.salary)
print(prajwal._protect)
print(prajwal._Employee__private)