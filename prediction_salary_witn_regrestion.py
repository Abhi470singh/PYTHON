import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r"C:\Users\aka90\Desktop\sql\Salary_Data.csv")

x = data.iloc[:,:-1]
y = data.iloc[:, -1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test, = train_test_split(x,y,train_size=.7,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

comparison = pd.DataFrame({'Actual': y_test,'Predicted': y_pred})
print(comparison)

plt.scatter(x_test, y_test, color="red")
plt.plot(x_train, regressor.predict(x_train), color ="blue")
plt.title('Salary vs Experience(test set)')
plt.xlabel('year of experience')
plt.ylabel('Salary')
plt.show()

m_slope = regressor.coef_
print(m_slope)

c_intercept = regressor.intercept_
print(c_intercept)

y_12 = (m_slope*12) + c_intercept
print(y_12)

y_20 = (m_slope*20) + c_intercept
print(y_20)

# 08/JULY/ 2025

 data.mean()

data['Salary'].mean()

data.median()

data['Salary'].median()

data.mode()
# coefficient of variation
from scipy.stats import variation
variation(data.values)

variation(data['Salary'])
data.corr()

 data['Salary'].corr(data['YearsExperience'])

data.skew()
data['Salary'].skew()

data.sem() # standard Error 

data['Salary'].sem()

import scipy.stats as stats
data.apply(stats.zscore)

stats.zscore(data['Salary'])
# degree of freedom
a=data.shape[0] # rows
b = data.shape[1]# columns
degree_of_freedom=a-b
print(degree_of_freedom)

y_mean =np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

#Error# ssc  sum of squre
y =y[0:6]
y_pred = y_pred[:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)


SST = SSR+SSE
print(SST)
r_square = 1- (SSR/SST)
r_square


bias = regressor.score(x_train,y_train)
print(bias)

variance=regressor.score(x_train,y_train)
print(variance)

from sklearn.metrics import mean_squared_error
y_test = y_test[:6]
train_mse = mean_squared_error(y_train,regressor.predict(x_train))
test_mse = mean_squared_error(y_test, y_pred)

import pickle
filename = 'Linear_ regression_model.pkl'

with open (filename,'wb') as file:
    pickle.dump(regressor,file)
print('Modelhas been picked and saved a Linear_Regressoion_model.pickle')

import os
os.getcwd()

