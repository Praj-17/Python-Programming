
import pandas as pd
from sklearn import linear_model
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor
from sklearn.linear_model import ARDRegression
from sklearn.linear_model import LogisticRegression
import numpy as np

#___________Reading the test and train datasets________
train_data = pd.read_csv('E:\\DATA SETS\\Simple regression data\\train.csv')
train = train_data.dropna() #__Training data_____

#Dropna() will remove any anomlies if present

test_data = pd.read_csv('E:\\DATA SETS\\Simple regression data\\test.csv')
test = test_data.dropna() #__Testing data_____

# print(train_data)
# print(test_data)
#___________Creating the variables _____
x_train = np.array(train.iloc[:,:-1].values) #Independant variable (Experience)
y_train =np.array(train.iloc[:,1].values)   #Dependant variable (Salary)
# x_train.reshape(23)
# x_train_2d = np.reshape(x_train,(23,2))
# print(x_train_2d.shape)

# print(x_train)
# print(y_train)
x_test = np.array(test.iloc[:,:-1].values) #Independant variable (Experience)
y_test =np.array(test.iloc[:,1].values)   #Dependant variable (Salary)

# print(x_test)
# print(y_test)
#________Training the model______

# model = linear_model.LinearRegression()
# model = tree.DecisionTreeRegressor()
# model = tree.ExtraTreeRegressor()
# model = linear_model.ARDRegression()
model = linear_model.LogisticRegression()
model.fit(x_train, y_train)

#_______Predicting from the model____
Prediction = model.predict(x_test)
print(Prediction)
#We will provide it an independant variable and it will print the dependant ones

#_________Accuracy____
Accuracy = model.score(x_test, y_test)
print(Accuracy)