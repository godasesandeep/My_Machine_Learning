# Classifier : User Defined K Nearest Neighbour
# DataSet    : Iris DataSet
#Features  : sepal width,,sepal lenght,petal width,petal lenght
#Lable     : 'versicolor','setosa','virginica'
#Traning Dataset : 135 Entries
#Testing Dataset  : 15 Entries


from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return distance.euclidean(a,b)

class UserDefinedKNN():
    def fit(self,trainingData,TrainingTarget):
        self.TrainingData = trainingData
        self.Trainingtarget = TrainingTarget

    def closest(self,row):
        bestdistance=euc(row,self.TrainingData[0])
        bestindex=0
        for i in range(1,len(self.TrainingData)):
            dist=euc(row,self.TrainingData[i])
            if dist < bestdistance:
                bestdistance=dist
                bestindex=i
        return self.Trainingtarget[bestindex]
    
    def predict(self,TestData):
        predictions =[]
        for row in TestData:
            lebel=self.closest(row)
            predictions.append(lebel)
        return predictions
    

        
def UserDefinedKNeighbor():
    

    iris=load_iris()
    data =iris.data
    target=iris.target

    data_train,data_test,target_train,target_test=train_test_split(data,target,test_size=0.1) #10% test data set

    '''border="-"*50
    print(border)
    print("Actual data set")
    print(border)

    for i in range(len(iris.target)):
        print("ID: %d,Label : %s Features %s" %(i,iris.data[i],iris.target[i]))
    print("Size of Actual data set %d"%(i+1))

    print(border)
    print("Training data set")
    print(border)
    for i in range(len(data_train)):
        print("ID: %d,Label %s,Feature:%s"%(i,data_train[i],target_train[i]))
    print("size of Test data set %d"%(i+1))

    print(border)
    print("Test data set")
    print(border)
    for i in range(len(data_test)):
        print("ID: %d,Label %s,Feature:%s"%(i,data_test[i],target_test[i]))
    print("size of Test data set %d"%(i+1))'''

    classifier = UserDefinedKNN()
    classifier.fit(data_train,target_train)
    predictions =classifier.predict(data_test)
    Accuracy=accuracy_score(target_test,predictions)
    print("Actual lable : ",target_test)
    print("Predicted lable : ",predictions)
    return Accuracy
    
def main():

    Accuracy = UserDefinedKNeighbor()
    print("Accuracy of classification algorithm with K Neighbor classifier is",Accuracy*100,"%")

if __name__=="__main__":
    main()