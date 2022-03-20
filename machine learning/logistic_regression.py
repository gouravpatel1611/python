from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt 


iris = datasets.load_iris()

x =  iris['data']
y = (iris['target'] ==2).astype(int)

clf = LogisticRegression()
clf.fit(x, y)
ex = clf.predict(([[6.7, 3.3, 5.7 ,1.5]]))
print(ex)

# x_new = np.linspace(0, 3,1000).reshape(-1,1)
# y_prob = clf.predict_proba(x_new)

# plt.plot(x_new,y_prob[:,1])
# plt.show()



# print(iris['data'].shape)
# print(iris['data'])
# print(iris['target'])
# print((iris.keys()))
 