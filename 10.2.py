#Unsupervised Hierarchical Clustering Problem
# All original points are considered single point clusters
#the two closes clusters will join and make a cluster
#Take the distance between clusters for the dendogram
#draw the largest verticle line and draw a perpendicular line, that is the optimal number of clusters

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Feature 1': [1.0, 1.5, 5.0, 8.0, 1.0, 9.0, 8.0, 10.0, 9.0, 10.0],
    'Feature 2': [2.0, 1.8, 8.0, 8.0, 0.6, 11.0, 2.0, 2.0, 3.0, 4.0]
}

df = pd.DataFrame(data)

# Extracting features for clustering
X = df[['Feature 1', 'Feature 2']]

import scipy.cluster.hierarchy as sch
dedndogram = sch.dendrogram(sch.linkage(X, method= 'ward'))
plt.title('DGram')
plt.xlabel("Customers")
plt.ylabel('Euclidian Distance')
plt.show()

from sklearn.cluster import AgglomerativeClustering
hc= AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')

df['Cluster'] = hc.fit_predict(X)


# Plotting the clusters
plt.scatter(df['Feature 1'], df['Feature 2'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Hierarchical Clustering')
plt.show()

