#Ensemble learning- when a single model uses multiple models internally
# If you get new data you can add it to the original model to get a second version
#Two type of models- Live models, Offline models
#Logistic regression is a classification model (Best when  the outcome is binary(Yes/no etc))
#Logistic Regression calculates probability of something happening
#log(p/1-p)= wx+b
# After interim probability is calculated, you have to provide a cutoff values. 
#To find the best cutoff value we use the ROC curve.
#You can covert/call r to python using libraries
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#
data = {
    'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 
                     7.0, 6.4, 6.9, 5.5, 6.5, 5.7, 6.3, 4.9, 6.6, 5.2,
                     5.5, 5.0, 4.9, 4.7, 5.1, 5.6, 4.8, 5.4, 5.7, 4.5, 
                     7.1, 6.3, 6.5, 6.7, 6.8, 6.9, 6.1, 5.8, 6.0, 5.7],
    'sepal_width': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 
                    3.2, 3.2, 3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7,
                    3.8, 3.2, 3.1, 3.0, 3.6, 3.4, 3.0, 3.1, 3.2, 3.5,
                    3.0, 2.7, 2.8, 3.0, 3.1, 2.9, 3.3, 3.4, 3.0, 2.8],
    'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5,
                     4.7, 4.5, 4.9, 4.0, 4.6, 4.5, 6.0, 3.3, 4.6, 3.9,
                     1.4, 1.5, 1.6, 1.4, 1.5, 1.7, 1.6, 1.5, 1.6, 1.4,
                     4.5, 4.9, 4.7, 4.8, 4.6, 4.7, 5.0, 4.3, 4.2, 4.8],
    'petal_width': [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1,
                    1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 2.5, 1.0, 1.3, 1.4,
                    0.2, 0.2, 0.4, 0.3, 0.2, 0.3, 0.4, 0.3, 0.2, 0.3,
                    1.6, 1.5, 1.7, 1.4, 1.8, 1.5, 1.6, 1.4, 1.7, 1.5],
    'species': ['setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
                'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
                'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
                'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor']
}

df = pd.DataFrame(data)


x= df.iloc[:,0:4].values
y= df.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test= train_test_split(x,y, test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test= sc_x.transform(x_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0,class_weight='balanced')
classifier.fit(x_train,y_train)

y_pred= classifier.predict(x_test)
print(y_pred)
print(y_test)
from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test, y_pred)
print(cm)
