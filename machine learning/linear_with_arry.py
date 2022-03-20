import matplotlib.pyplot as plt
import numpy as np 
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

#dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])

diabetes = datasets.load_diabetes()

diabetes_x = np.array([[1],[2],[3]])

diabetes_x_train = diabetes_x
diabetes_x_test = diabetes_x

diabetes_y_train = np.array([3,2,4])
diabetes_y_test = np.array([3,2,4])

model = linear_model.LinearRegression()
model.fit(diabetes_x_train, diabetes_y_train)
diabetes_y_predict =  model.predict(diabetes_x_test)

#mean squared error is:  3035.0601152912695
print("mean squared error is: ",mean_squared_error(diabetes_y_test,diabetes_y_predict))
print("weigths :",model.coef_)
print("Intercept: ",model.intercept_)

plt.scatter(diabetes_x_test, diabetes_y_test)
plt.plot(diabetes_x_test,diabetes_y_predict)
plt.show()




