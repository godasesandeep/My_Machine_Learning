#Classifier: Decision Tree 
#DataSet   : Iris Dataset
#Features  : sepal width,,sepal lenght,petal width,petal lenght
#Lable     : 'setosa', 'versicolor', 'virginica'
#Traning Dataset : 147 Entries
#Testing Dataset  : 3 Entries

import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

#load data

Data=load_iris()

#print(Data)

#{'data': array([[5.1, 3.5, 1.4, 0.2], [4.9, 3. , 1.4, 0.2]......]
#'target': array([0, 0, 0, 0.....]
#'target_names': array(['setosa', 'versicolor', 'virginica']
#'feature_names': ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
#}

# First 50 data : Sentosa -->0  ,next 50 data : Versicolor -->1 ,Next 50 data : Virginica -->2

#Indices removed for Test or prediction purpose

test_index = [1,51,101]

#Traning data with elemunited Test Indices
train_target =np.delete(Data.target,test_index)
train_data = np.delete(Data.data,test_index,axis=0)

#Testing data for testing Model
test_target = Data.target[test_index]
test_data = Data.data[test_index]

#Model Decision Tree classifier 

clf =tree.DecisionTreeClassifier()

#Train the model 

clf.fit(train_data,train_target)

#Test for given value

pred = clf.predict(test_data)

print("Actual Value :  ",Data.target[test_index])
print("Predicted value : ",pred)

