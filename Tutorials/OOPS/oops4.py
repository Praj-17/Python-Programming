#Multilevel Inheritence
class Dad:
    basketball = 1
class Son(Dad):
   Dancing = 1
   basketball = 2
   def isdance(self):
       return f"Yes I dance {self.Dancing} no of times"
class Grandson(Son):
    Dancing = 6
    
    def isdance(self):
       return f"Yes I dance at most {self.Dancing} no of times"

Darry = Dad()  
Larry =Son()  
Harry = Grandson()  
print(Harry.isdance())
print(Harry.basketball)

