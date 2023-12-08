
#Classifier: K-Means
#DataSet   : Iris Dataset
#Features  : sepel lenth,sepal width,petal lenght,petal width
#Lable     : No lable ,K=3
#Traning Dataset : 150 Entries
#Testing Dataset  : 150 Entries


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

#load data


X, y = load_iris(return_X_y=True)

'''fig = plt.figure(0)
plt.grid(True)
plt.scatter(X[:,0],X[:,1])
plt.show()'''

#Initialize the random centroids


k = 3
 
clusters = {}
np.random.seed(23)
 
for idx in range(k):
    #center = 2*(2*np.random.random((X.shape[1],))-1)
    center = X[idx]
    points = []
    cluster = {
        'center' : center,
        'points' : []
    }
     
    clusters[idx] = cluster
     
print(clusters)

#Plot the random initialize center with data points


'''plt.scatter(X[:,0],X[:,1])
plt.grid(True)
for i in clusters:
    center = clusters[i]['center']
    plt.scatter(center[0],center[1],marker = '*',c = 'red')
plt.show()'''

#Define euclidean distance


def distance(p1,p2):
    return np.sqrt(np.sum((p1-p2)**2))

#Create the function to Assign and Update the cluster center


#Implementing E step 
def assign_clusters(X, clusters):
    for idx in range(X.shape[0]):
        dist = []
         
        curr_x = X[idx]
         
        for i in range(k):
            dis = distance(curr_x,clusters[i]['center'])
            dist.append(dis)
        curr_cluster = np.argmin(dist)
        clusters[curr_cluster]['points'].append(curr_x)
    return clusters
         
#Implementing the M-Step
def update_clusters(X, clusters):
    for i in range(k):
        points = np.array(clusters[i]['points'])
        if points.shape[0] > 0:
            new_center = points.mean(axis =0)
            clusters[i]['center'] = new_center
             
            clusters[i]['points'] = []
    return clusters

#Create the function to Predict the cluster for the datapoints


def pred_cluster(X, clusters):
    pred = []
    for i in range(X.shape[0]):
        dist = []
        for j in range(k):
            dist.append(distance(X[i],clusters[j]['center']))
        pred.append(np.argmin(dist))
    return pred


#Assign, Update, and predict the cluster center
for i in range(500):
    clusters = assign_clusters(X,clusters)
    clusters = update_clusters(X,clusters)
pred = pred_cluster(X,clusters)

#Plot the data points with their predicted cluster center

'''plt.scatter(X[:,0],X[:,1],c = pred)
for i in clusters:
    center = clusters[i]['center']
    plt.scatter(center[0],center[1],marker = '^',c = 'red')
plt.show()'''

print(pred)


plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.scatter(X[:,0],X[:,1],c = pred, cmap=cm.Accent)
plt.grid(True)
for i in range(k):
    centern=clusters[i]['center']
    center = centern[:2]
    plt.scatter(center[0],center[1],marker = '^',c = 'red')
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
     
plt.subplot(1,2,2)   
plt.scatter(X[:,2],X[:,3],c = pred, cmap=cm.Accent)
plt.grid(True)
for i in range(k):
    centern=clusters[i]['center']
    center = centern[2:4]
    plt.scatter(center[0],center[1],marker = '^',c = 'red')
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.show()
