import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv(r"C:\Users\aka90\Desktop\abhi vs code\spyder code machine learning\Investment.csv")

x = dataset.iloc[:,:-1]
y = dataset.iloc[:,4]

x=pd.get_dummies(x,dtype=int)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

bais=regressor.score(x_train,y_train)
bais

variance=regressor.score(x_test,y_test)
variance

slope= regressor.coef_
print(slope)

intercept=regressor.intercept_
print(intercept)

x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)

import statsmodels.api as sm
x_opt= x[:,[0,1,2,3,4,5]]
regressor_ols=sm.OLS(endog=y,exog=x_opt).fit
regressor_ols.summary()

import statsmodels.api as sm
x_opt= x[:,[0,1,2,3,4,5]]
regressor_ols=sm.OLS(endog=y,exog=x_opt).fit
regressor_ols.summary()

import statsmodels.api as sm
x_opt= x[:,[0,1,2,3,4,5]]
regressor_ols=sm.OLS(endog=y,exog=x_opt).fit
regressor_ols.summary()

import statsmodels.api as sm
x_opt= x[:,[0,1,2,3,4,5]]
regressor_ols=sm.OLS(endog=y,exog=x_opt).fit
regressor_ols.summary()

import statsmodels.api as sm
x_opt= x[:,[0,1,2,3,4,5]]
regressor_ols=sm.OLS(endog=y,exog=x_opt).fit
regressor_ols.summary()

























