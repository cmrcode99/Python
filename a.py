import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


#Step 1 find target
#Seperate X and Y
dataset= pd.read_csv(r"C:\Users\cmrgu\OneDrive\Desktop\Python_Project\data.csv")
x= dataset.iloc[:,0:3].values
y= dataset.iloc[:,3].values
#Step 2 Data Preprocessing
#Replace Nan with mean
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer= imputer.fit(x[:,1:3])
x[:,1:3]= imputer.transform(x[:,1:3])


#Taking care of Strings/ Categorival
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_x= LabelEncoder()
x[:,0]= labelencoder_x.fit_transform(x[:,0])
ct= ColumnTransformer([("Country", OneHotEncoder(), [0])], remainder="passthrough")
x= ct.fit_transform(x)
#for y column one hot encoding not necessary only x col in machine learning, except in deep learning

labelencoder_y= LabelEncoder()
y= labelencoder_y.fit_transform(y)
print(y)
#Split the data into two sets- Training Set and the Test Set
from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test= train_test_split(x,y, test_size=0.2,random_state=0)
#Then you Feature Scale(Normalization)
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test= sc_x.transform(x_test)





#Step 3: Training = Data + Algo= Model
#supervised ML xand y are known- Classification, Regression
#unsupervised only x is known- Clustering
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_train,y_train)
a=regressor.score(x_train,y_train)
regressor.coef_
regressor.intercept_
y_pred= regressor.predict(x_test)

#visualize the data
plt.scatter(x_train, y_train, color = "red")
plt.plot(x_train, regressor.predict(x_train), color="blue")
plt.xlabel
plt.ylabel
