# the sequence in which u put the names in the inherited class matters!
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
#print(harry.salary)
class player:
    var = 9
    no_of_games = 4
    def __init__(self, name , game) -> None:
        self.name = name
        self.game = game
    def printdetails(self):
        return f"Name is {self.name}, Game is {self.game}"
class cool_Programmer(Employee, player):
    pass
    
shubham = player("shumbham", ["Cricket"])
karan = cool_Programmer("karan", "8999", "cool programmer")
det = karan.printdetails()
print(det)
print(karan.var)
print(shubham.var)



        
        