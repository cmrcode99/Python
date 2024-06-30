import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#This is a NLP use case

#Import the dataset

# In an NLP where there is sentences, all unique words will become a column name, this is a way to convert the strings to numbers

# Remove all non alphabet characters next 

#convert everything to same case

#remove prepositions/stop words(is, and , the, an, of, for...)

#remove stemming(love,loving,lovable>love, walk, walking, walks>walk)

#The Lemmatize|Synonyms (Jump , hop > jump)

#Select top 1500 commonly occuring words(but this might drop info)
dataset= pd.read_csv(r'C:\Users\cmrgu\Downloads\Restaurant_Reviews.tsv', sep='/t', header=0 )
print(dataset)
# library to clean data
import re 

# Natural Language Tool Kit
import nltk 

nltk.download('stopwords')

# to remove stopword
from nltk.corpus import stopwords

# for Stemming propose 
from nltk.stem.porter import PorterStemmer

# Initialize empty array
# to append clean text 
corpus = [] 


# 1000 (reviews) rows to clean
for i in range(0, 1000): 
	
	# column : "Review", row ith
	review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
	
	# convert all cases to lower cases
	review = review.lower() 
	
	# split to array(default delimiter is " ")
	review = review.split() 
	
	# creating PorterStemmer object to
	# take main stem of each word
	ps = PorterStemmer() 
	
	# loop for stemming each word
	# in string array at ith row 
	review = [ps.stem(word) for word in review
				if not word in set(stopwords.words('english'))] 
				
	# rejoin all string array elements
	# to create back into a string
	review = ' '.join(review) 
	
	# append each string to create
	# array of clean text 
	corpus.append(review) 

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer

# To extract max 1500 feature.
# "max_features" is attribute to
# experiment with to get better results
cv = CountVectorizer(max_features = 1500) 

# X contains corpus (dependent variable)
X = cv.fit_transform(corpus).toarray() 

# y contains answers if review
# is positive or negative
y = dataset.iloc[:, 1].values 

# Splitting the dataset into
# the Training set and Test set
from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test= train_test_split(X,y, test_size=0.2,random_state=0)

# Fitting Naives Bayes
# to the Training set
from sklearn.naive_bayes import GaussianNB

model= GaussianNB()
model.fit(x_train, y_train) 

# Predicting the Test set results
y_pred = model.predict(x_test)
