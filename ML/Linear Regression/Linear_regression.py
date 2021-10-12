import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error
#Importing datasets
diabetes = datasets.load_diabetes()
# print(diabetes.keys())
# ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'] The list of keys
# print(diabetes.data)
# print(diabetes.DESCR)

diabetes_x = diabetes.data #creates an array of array which will be x axis
# print(diabetes_x)

#Partitioning x
diabetes_x_train = diabetes_x[:-30]
diabetes_x_test = diabetes_x[-30:]

#Partitioning y
diabetes_y_train = diabetes.target [:-30]
diabetes_y_test = diabetes.target [-30:]

#Calling the imp function
model = linear_model.LinearRegression()

#Fitting the data 
model.fit(diabetes_x_train,diabetes_y_train)
#Predicting the outcome
diabetes_y_predicted=model.predict(diabetes_x_test)

#Printing the mean squared error
print("the mean squared error is: ", mean_squared_error(diabetes_y_test, diabetes_y_predicted))

#plotting the model
print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)

#scatter plot
# plt.scatter(diabetes_x_test, diabetes_y_test)
# plt.plot(diabetes_x_test, diabetes_y_predicted)
# plt.show()