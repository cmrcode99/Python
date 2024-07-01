# Dimensional Reduction
# -Feature Selection(Extracting columns)
# P value being statistically significant

# Feature Extracting- Take new columns from existing columns
# PCA(Principle Component Extraction)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
a= load_wine()
from sklearn.model_selection import train_test_split
x= a.get('data')
y=a.get('target')
df= pd.DataFrame(x)
df1= pd.DataFrame(y)
X= df.iloc[:,:].values
Y=df1.iloc[:,:].values
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(X,Y,random_state=0, test_size=0.2)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train= sc.fit_transform(x_train)
x_test=sc.transform(x_test)

from sklearn.decomposition import PCA
pca= PCA(n_components=2)
x_train= pca.fit_transform(x_train)
x_test= pca.transform(x_test)
explained_variance = pca.explained_variance_ratio_

from sklearn.linear_model import LogisticRegression
classifier= LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)

y_pred= classifier.predict(x_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)
