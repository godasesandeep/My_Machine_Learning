from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

#Load DataSet

Data = load_iris()

train_data,test_data,train_feature,Test_feature = train_test_split(Data.data,Data.target,test_size=0.2) #20% test data

dtc = tree.DecisionTreeClassifier()
dtc.fit(train_data,train_feature)
dtcPred=dtc.predict(test_data)

knn = KNeighborsClassifier()
knn.fit(train_data,train_feature)
knnPred=knn.predict(test_data)

dtcAccuracy = accuracy_score(Test_feature,dtcPred)
knnAccuracy = accuracy_score(Test_feature,knnPred)

print("Decision Tree Classifier Accuracy : ",dtcAccuracy*100)
print("K Nearest Keighbors Classifier Accuracy : ",knnAccuracy*100)