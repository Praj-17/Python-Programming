import random
import numpy 
random_number = random.randint(0,5)
print(random_number)
rand = random.random() *100
print(rand)
list = ["star plus", "aaj tak", "DD1"]
choice = random.choice(list)
print(choice)
x = numpy.arange(10)
choice2 = random.choice(x)
print(choice2)