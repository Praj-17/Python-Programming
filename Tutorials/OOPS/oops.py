# class student:
#     pass
# harry = student()
# prajwal = student()
# print(harry, prajwal)

# prajwal.name = "prajwal"
# prajwal.age = 19
# prajwal.std = "fy"

# harry.std = 12
# harry.subjects = ["maths", "chem"]
# print(prajwal.name, prajwal.age, harry.subjects)
from ast import Param


class Employee:
    no_of_leaves = 8
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

# prajwal.salary = 45
# prajwal.name = "prajwal"
# prajwal.company = "google"

# Aishu.salary = 45
# Aishu.name = "Aishu"
# Aishu.company = "Microsoft"

# print(prajwal.printdetails())
# print(Aishu.printdetails())
# print(Aishu.no_of_leaves)
# Aishu.no_of_leaves = 9
# print(Aishu.no_of_leaves)
# print(prajwal.no_of_leaves)
# Employee.no_of_leaves =10
# print(prajwal.no_of_leaves)
# print(Aishu.no_of_leaves)