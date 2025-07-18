import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv(r"C:\Users\aka90\Downloads\emp_sal.csv")
X =dataset.iloc[:,1:2].values
y =dataset.iloc[:, 2].values

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

plt.scatter(X, y, color = 'red')
plt.plot(X,lin_reg.predict(X), color = 'blue')
plt.title('Linear regression model (Linear Regression)')
plt.xlabel('Position')
plt.ylabel('salary')
plt.show()

lin_model_pred = lin_reg.predict([[6]])
lin_model_pred

from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)

lin_reg_2= LinearRegression()
lin_reg_2.fit(X_poly, y)

plt.scatter(X, y, color = 'red')
plt.plot(X,lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('polynomail (Polynomail Regression)')
plt.xlabel('Position Leval')
plt.ylabel('salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred


from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)

lin_reg_2= LinearRegression()
lin_reg_2.fit(X_poly, y)

plt.scatter(X, y, color = 'red')
plt.plot(X,lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('polynomail (Polynomail Regression)')
plt.xlabel('Position Leval')
plt.ylabel('salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred

from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)

lin_reg_2= LinearRegression()
lin_reg_2.fit(X_poly, y)

plt.scatter(X, y, color = 'red')
plt.plot(X,lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('polynomail (Polynomail Regression)')
plt.xlabel('Position Leval')
plt.ylabel('salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred

from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=5)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)

lin_reg_2= LinearRegression()
lin_reg_2.fit(X_poly, y)

plt.scatter(X, y, color = 'red')
plt.plot(X,lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('polynomail (Polynomail Regression)')
plt.xlabel('Position Leval')
plt.ylabel('salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred



# svr Using kernel 16/07/2025
from sklearn.svm import SVR 
svr_reg = SVR(kernel="poly",degree=5)
svr_reg.fit(X, y)
svr_pred = svr_reg.predict([[6]])
print(svr_pred)



from sklearn.svm import SVR 
svr_reg = SVR(kernel="poly",degree=6,gamma="scale")
svr_reg.fit(X, y)
svr_pred = svr_reg.predict([[6]])
print(svr_pred)


from sklearn.svm import SVR 
svr_reg = SVR(kernel="sigmoid",degree=4)
svr_reg.fit(X, y)
svr_pred = svr_reg.predict([[6]])
print(svr_pred)

from sklearn.svm import SVR 
svr_reg = SVR(kernel="rbf",degree=4)
svr_reg.fit(X, y)
svr_pred = svr_reg.predict([[6]])
print(svr_pred)

# knn(k neares neighbour) Model
from sklearn.neighbors import KNeighborsRegressor
knn_reg =KNeighborsRegressor(n_neighbors=3)
knn_reg.fit(X, y) 

knn_pred = knn_reg.predict([[6]])
print(knn_pred)

from sklearn.neighbors import KNeighborsRegressor
knn_reg =KNeighborsRegressor(n_neighbors=2)
knn_reg.fit(X, y) 

knn_pred = knn_reg.predict([[6]])
print(knn_pred)

from sklearn.neighbors import KNeighborsRegressor
knn_reg =KNeighborsRegressor(n_neighbors=1)
knn_reg.fit(X, y) 

knn_pred = knn_reg.predict([[6]])
print(knn_pred)


# decision tree
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor()
dt_reg.fit(X,y)

dt_pred = dt_reg.predict([[6]])
print(dt_pred)


# randaom forest
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor()
rf_reg.fit(X,y)
rf_pred = rf_reg.predict([[6]])
print(rf_pred)

from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(random_state=0)
rf_reg.fit(X,y)
rf_pred = rf_reg.predict([[6]])
print(rf_pred)













