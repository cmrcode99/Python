#Unsupervised Machine learning(No clear y value)
#-KMeans and Hierarchical Clustering

#KMeans- Find optimal number of clusters with elbow methods
#Kmeans works by making k number of random centroids, these centroids continously get made until equilibrium is reached.

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

#Elbow Method for optimal number of clusters
wcss= []
for i in range(1,10):
    kmeans= KMeans(n_clusters=i, init="k-means++", random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,10),wcss)
plt.title("Elbow Method")
plt.xlabel('Number 0f Clusters')
plt.ylabel('Wcss')
plt.show()
#The lowest cluster with a sharp turn is the number of clusters you use
#That is the sharpest change in the wcss

# Applying KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)


# Plotting the clusters
plt.scatter(df['Feature 1'], df['Feature 2'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-means Clustering')
plt.show()

#the goal of unsupervised learning is to understand patterns using clusters. 
