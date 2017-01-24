import pandas as pd
import numpy as np
from sklearn import preprocessing, svm, cross_validation
from sklearn.linear_model import LinearRegression

df = pd.read_csv('wine_data.csv')
    
#print df.head()

X = np.array(df.drop(['class'], 1)) # everything except for label
X = preprocessing.scale(X) # not available for real-time data
#df.dropna(inplace=True)
y = np.array(df['class'])

print 'model 1'
acc=[]
for i in range(10):
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.5)    
    classifier = LinearRegression()
    classifier.fit(X_train, y_train)
    #Testing the model with accuracy
    accuracy = classifier.score(X_test, y_test)
    #print accuracy
    acc.append(accuracy)
print sum(acc)/len(acc)

print 'model 2'
acc1 = []    
for i in range(10):
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.5)
    classifier1 = svm.SVR(kernel = 'linear')
    #Fitting the training data to the model
    classifier1.fit(X_train, y_train)
    #Testing the model with accuracy
    accuracy = classifier1.score(X_test, y_test)
    #print accuracy
    acc1.append(accuracy)
print sum(acc1)/len(acc1)

print 'model 3'
#Model 3
#Support Vector Machine using polynomial kernel
acc2 = []
for i in range(10):
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.5)
    classifier2 = svm.SVR(kernel = 'poly')
    #Fitting the training data to the model
    classifier2.fit(X_train, y_train)
    #Testing the model with accuracy
    accuracy = classifier2.score(X_test, y_test)
    #print accuracy
    acc2.append(accuracy)
print sum(acc2)/len(acc2)    