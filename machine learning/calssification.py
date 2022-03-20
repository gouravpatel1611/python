from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


# Loding data 
iris = datasets.load_iris()

# printing data
print(iris.DESCR)
features = iris.data
labels = iris.target
print(features[0],labels[0])

# traning the clasifire

clf = KNeighborsClassifier()
clf.fit(features,labels)

preds = clf.predict([[1,1,1,1]])
print(preds)