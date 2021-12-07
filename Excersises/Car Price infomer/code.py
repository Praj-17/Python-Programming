import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("E:\\DATA SETS\\2. Cars Data1.csv") # Place the path of your dataset here 
dataset = np.array(dataset)
# car_prices = dict(zip(model_name,[model_price, dataset['Cylinders'], dataset['EngineSize'], dataset['Horsepower'], dataset['Weight'], dataset['MPG_City'], dataset['MPG_Highway']]))
print("_____WELCOME TO CAR NAME INFORMER_______")
print("\n Please input the name of the model you wanna see price for")
car = input("Input: ")

for i in dataset: #SEARCING FOR THE PARTICULAR CAR
    for j in i:
        if j ==car:
            print("ok")
            a =i
            
print(a)
print("_______The price of the car is_______")
print(a[5])
print("_______The no of cylinders in the car is_______")
print(a[8])
print("_______The Type of the car is_______")
print(a[2])
print("_______The Engine Size is_______")
print(a[7])
print("_______The origin of the car is_______")
print(a[3])
print("_______The weight of the car is_______")
print(a[12])
print("_______The horsepower of the car is_______")
print(a[9])
print("_______The wheelbase of the car is_______")
print(a[13])
print("_______The length of the car is_______")
print(a[14])
print("_______The milage in city of the car is_______")
print(a[10])
print("_______The milage in highway of the car is_______")
print(a[11])
milages = [a[10], a[11]]



    