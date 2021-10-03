class Employee():
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
       # self.email =f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"This emloyee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set pls set it using setter"
        email =f"{self.fname}.{self.lname}@gmail.com"
        return email
    @email.setter
    def email(self,string):
       names =  string.split("@")[0]
       self.fname = names.split(".")[0]
       self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
    
    
       
Prajwal = Employee("prajwal", "waykos")
Aishu = Employee("Sakshi", "Aherkar") 
print(Prajwal.explain())
print(Prajwal.email)
Aishu.fname = "Aishu"
print(Aishu.email)
Aishu.email = "Sakshi.Aherkar@gmail.com"
print(Aishu.email)
del Prajwal.email
print(Prajwal.email)

        