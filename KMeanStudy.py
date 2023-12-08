
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs



X,y = make_blobs(n_samples = 10,n_features = 2,centers = 3,random_state = 23) # Generate data points n-Sample * n_Features
print(X) # Generated sample point matrix of n-Sample * n_Features
print(y) #Feature output matrix for clusters of size n_sample
print(X[:,0]) #x value ,value of 1st feature
print(X[:,1]) #y value ,value of 2st feature
print(X.shape) #Print size of X (n_sample,n_feature)
print(X.shape[1])# second value in size of X (n_sample,n_feature)==>n_feature
print(X[0])#First value in X matrix ,i.e first value of sample in n_samples
p=2*(2*np.random.random((X.shape[1],))-1) #generate random center point for cluster
print(p)
p1=X[0] # Point 1
p2=X[1] # Point 2
print(type(X[1]))  # 'numpy.ndarray'
d=np.sqrt(np.sum((p1-p2)**2)) # euclidian distance betn point 1 and point 2
print(d)
dist=[5,10,15]
dmin=np.argmin(dist) #Gives minimum value position
print(dmin)
#fig = plt.figure(0)
#plt.grid(True)
#plt.scatter(X[:,0],X[:,1])
#plt.show()
