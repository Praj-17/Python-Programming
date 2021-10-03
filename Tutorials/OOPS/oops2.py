


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

class Programmer(Employee):
    def __init__(self, aname, asalary, acompany, alangguages):
        super().__init__(aname, asalary, acompany)
        Programmer.langguages = alangguages
    def printprogrammer(Self):
        return f"The programmer name is {Self.name} salary is {Self.salary} and company is {Self.company} and he knows {Self.alangguages}"
    
    
    
Shubham = Programmer("shubham", 55, "apple", ["python"])
karan = Programmer("karan", 565, "google", ["python"])

print(karan.printprogrammer())