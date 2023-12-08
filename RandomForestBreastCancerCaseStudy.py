import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#Load Diabetes Dataset
dataset =pd.read_csv("breast-cancer-wisconsin.csv")

#Get basic statics of loaded data
#print(dataset.describe())

#Filter Missing Values -->Drop the missing values row from the dataset
print(dataset.columns[6])

dataset=dataset[dataset["BareNuclei"]!='?']
print("Size of dataset : ",dataset.shape)
#Split data in train & test 

train_data,test_data,train_lebal,test_lebal=train_test_split(dataset[dataset.columns[1:-1]],dataset[dataset.columns[-1]],test_size=0.3)

print("Train data Size : ",train_data.shape)
print("Test data Size : ",test_data.shape)
print("Train lebal Size : ",train_lebal.shape)
print("Test lebal Size : ",test_lebal.shape)

#Train the model

clf= RandomForestClassifier()
clf.fit(train_data,train_lebal)

#Predict the output

pred = clf.predict(test_data)

print("First 25 Outcomes")
for i in range(0,26):
    print("Actual outcome :: {} and Predicted Outcome :: {}".format(list(test_lebal)[i],pred[i]))

print("Train Accuracy : ",accuracy_score(train_lebal,clf.predict(train_data))*100)
print("Test Accuracy : ",accuracy_score(test_lebal,pred)*100)
print("Confusion Matrix : ",confusion_matrix(test_lebal,pred))