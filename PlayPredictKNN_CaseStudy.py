#Classifier : K Nearest Neighbour
#DataSet    : Play Predictor DataSet
#Features   : Whether ,Temperature
#Lable      : Yes,No
#Traning DataSet  : 30 Entries
#Testing Dataset  : 1 Entry

import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


def PlayPredictKNN(data_path,Iwhether,Itemp):

    #Load Data
    data =pd.read_csv(data_path,index_col=0)

    #Extract data
    whether=data.Whether
    Temp=data.Temperature
    Play=data.Play
    Pfeature=list(zip(whether[0:5],Temp[0:5]))
    print("First 5 Features : " ,Pfeature)
    #Lable Encding
    LE =preprocessing.LabelEncoder()
    whether_encod=LE.fit_transform(whether)
    Temp_encod=LE.fit_transform(Temp)
    Play_Lable=LE.fit_transform(Play)
    
    #Combine wheter & Temp feature
    features=list(zip(whether_encod,Temp_encod))
    print("First 5 encoded Features : " ,features[0:5])
    print("First 5 play Features : ",Play[0:5])
    print("First 5 encoded Play Fearures : ",Play_Lable[0:5])

    #Train data

    Model= KNeighborsClassifier(n_neighbors=3)

    Model.fit(features,Play_Lable)
    # Whether --> Overcast: 0 , 'Rainy':1 , 'Sunny' :2
    #Temperature -->'Cool' :0 , 'Hot' : 1, 'Mild':2

    Whether_dic={'overcast': 0 , 'rainy':1 , 'sunny' :2}
    Temperature_dic={'cool' :0 , 'hot' : 1, 'mild':2}

    Predicted = Model.predict([[Whether_dic[Iwhether.lower()],Temperature_dic[Itemp.lower()]]])  #0:Overcast,2:Mild
    print(Predicted)
    if Predicted[0]==0:
        print("Don't play")
    if Predicted[0]==1:
        print("You can Play")

def main():
    print("Play Predictor CaseStudy")
    Iwhether=input("Enter whether ['overcast', 'rainy', 'sunny']  :" )
    ITemp=input("Enter Temperature ['cool', 'hot', 'mild']  :" )
    if Iwhether.lower() in ['overcast', 'rainy', 'sunny'] and ITemp.lower() in ['cool', 'hot', 'mild'] :
        PlayPredictKNN("PlayPredictor.csv",Iwhether,ITemp)
    else:
        print("Error : Enter valid values of input")
        exit()
    

if __name__ =="__main__":
    main()



