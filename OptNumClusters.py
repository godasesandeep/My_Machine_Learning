# Finding the Optimum Number of cluster for K-Means Classification

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

#load data 
#dataset =pd.read_csv("iris.csv")
#X=dataset.iloc[:,[0,1,2,3,4]].values

X, y = load_iris(return_X_y=True)


#Optimum number of cluster finding

wcss=[]   #with in cluster sum of square  #SUM OF SQUARED ERROR
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",max_iter=300,n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

#Plot tehe results onto line graph no cluster VS wcss

plt.plot(range(1,11),wcss)
plt.grid(True)
plt.title("Elbow method")
plt.xlabel("Number of cluster")
plt.ylabel("WCSS")
plt.show()

#Apply kmeans to the dataset /creating the kmeans classifier
kmeans=KMeans(n_clusters=3,init="k-means++",max_iter=300,n_init=10,random_state=0)
#kmeans.fit(X)
y_pred=kmeans.fit_predict(X)
#print(y_pred)

#Visualising the clusters

plt.scatter(X[y_pred==0,0],X[y_pred==0,1],s=100,c='red',label='Iris-setosa')

plt.scatter(X[y_pred==1,0],X[y_pred==1,1],s=100,c='blue',label='Iris-Versicolour')

plt.scatter(X[y_pred==2,0],X[y_pred==2,1],s=100,c='green',label='Iris-Virginica')

#Plotting the centroids of the clusters

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='yellow',label='Centroids')

plt.legend()

plt.show()