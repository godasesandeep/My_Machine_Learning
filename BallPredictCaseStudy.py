#Classifier: Desision Tree
#DataSet   : Ball Dataset
#Features  : Weight & Surface
#Lable     : Tennis and cricket
#Traning Dataset : 15 Entries
#Testing Dataset  : 1 Entries

from sklearn import tree

def PrdictBall(weight,surface):
    #0-->Smooth ,1-->Rough
    Ballfeatures=[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    #1-->Tennis ball ,2-->Cricket ball
    Name=[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    clf =tree.DecisionTreeClassifier()
    clf.fit(Ballfeatures,Name)
    result=clf.predict([[weight,surface]])
    if result == 1:
        print("Object looks like tennise ball")
    elif result==2:
        print("Object looks like Cricket ball")

def main():
    print("Predict ball case study")
    weight=input("Enter weight of ball   :")
    surface=input("Enter type of surface : [smooth or rough]   :")
    if surface.lower()=='rough':
        surface=1
    elif surface.lower()=='smooth':
        surface=0
    else:
        print("Error:Wrong input")
        exit()
    PrdictBall(weight,surface)

if __name__=="__main__":
    main()