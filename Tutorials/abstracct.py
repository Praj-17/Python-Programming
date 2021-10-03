from abc import ABCMeta, abstractmethod
class Shape(metaclass = ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0 
        

class Rectangle:
    type = "rectangle"
    sides = 4
    def __init__(self ) -> None:
        self.length = 6
        self.breadth = 7
        
    def pritarea(self):
      area =   self.length * self. breadth
      print(area)
rect1 = Rectangle()
print(rect1.printarea())