#when u import a file into another file it also executes the first file to stop this problem we use if - name system
from typing import Mapping


def add(a,b):
    return a+b+5
def substract(a,b):
    return a-b-1
print("and the name is ", __name__)
if __name__ == '__main__':
    print(add(1,2))
    print(add(1,2))
    


