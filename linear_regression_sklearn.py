#This code was built as a part of exercise from tutorials on www.pythonprogramming.net

import pandas as pd
import quandl
import numpy as np
from sklearn import preprocessing, svm, cross_validation
from sklearn.linear_model import LinearRegression 

#Creating a data frame and getting google stock price using quandl
df = quandl.get('WIKI/GOOG')
#Getting only the essential variables
df = df[['Adj. Open', 'Adj. Close', 'Adj. High', 'Adj. Low', 'Adj. Volume']]
#Getting normalized varialbes which will help in better prediction
df['High_Low_PCT_Change'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100
df['Open_Close_PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

#taking only the useful variables
df = df[['Adj. Close', 'High_Low_PCT_Change', 'Open_Close_PCT_Change', 'Adj. Volume' ]]

#print df.head()
#print df[df['Adj. Volume'].isnull()]

#The forecast factor is used to decide how many days in advance do we want to predict
#Here 10% of 708 days will be 7 days
forecast_factor = int(round(0.01 * len(df)))
#The shift function is used for predication of 7 days in advance
df['Predicted Close Price'] = df['Adj. Close'].shift(-forecast_factor)
#Since we used shift of 7 days, we will have 7 missing values which we will get rid of
df.dropna(inplace=True)
#print df.head()
#print df[df['Predicted Close Price'].isnull()]

#Crerating numpy arrays to store data frames
X = np.array(df.drop(['Predicted Close Price'], 1))
#Scaling the data
X = preprocessing.scale(X)
y = np.array(df['Predicted Close Price'])

#Using cross validation to train and test the data
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

#Model 1
#Linear Regression
classifier = LinearRegression()
#Fitting the training data to the model
classifier.fit(X_train, y_train)
#Testing the model with accuracy
accuracy = classifier.score(X_test, y_test)
print accuracy

#Model 2
#Support Vector Machine using linear kernel
classifier1 = svm.SVR(kernel = 'linear')
#Fitting the training data to the model
classifier1.fit(X_train, y_train)
#Testing the model with accuracy
accuracy = classifier1.score(X_test, y_test)
print accuracy

#Model 3
#Support Vector Machine using polynomial kernel
classifier2 = svm.SVR(kernel = 'poly')
#Fitting the training data to the model
classifier2.fit(X_train, y_train)
#Testing the model with accuracy
accuracy = classifier2.score(X_test, y_test)
print accuracy