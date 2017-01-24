#This code was built with the help of tutorial videos on www.pythonprogramming.net

from __future__ import division
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import style
style.use('ggplot')

#y = mx + b
#Slope(m) = (NΣXY - (ΣX)(ΣY)) / (NΣX2 - (ΣX)2)
#Intercept(c) = (ΣY - b(ΣX)) / N
#x and y are the variables.
#m = The slope of the regression line 
#b = The intercept point of the regression line and the y axis.	
#N = Number of observations 
#ΣXY = Sum of the product of x and y
#ΣX = Sum of x
#ΣY = Sum of y
#ΣX2 = Sum of square x

x = np.array([0,1,6,4,13,11,16,10,14,19])
y = np.array([2,3,5,7,9,11,13,15,17,18])

#We will generate some random data first.
x1 = np.random.normal(3.0, 1.0, 100)
y1 = 10 - (x1 + np.random.normal(0, 0.1, 100)) * 3

#We define a function that returns slope and intercepts.
def slope_and_intercept(x, y):
    
    slope = (((mean(x)*mean(y)) - mean(x*y)) /
         ((mean(x)*mean(x)) - mean(x*x)))
    
    y_intercept = mean(y) - slope *mean(x)    
    
    print 'The slope is : ' + str(slope)
    print 'The value of Y Intercept is : ' + str(y_intercept)

    return slope, y_intercept

slope, y_intercept = slope_and_intercept(x, y)
slope1, y_intercept_1 =slope_and_intercept(x1 ,y1)  

def regress_line(x):
    regression_line = []
    for i in x:
        regression_line.append((slope*i)+y_intercept)
    return regression_line     
    
  

l = regress_line(x)

predict_x = np.array([3,8,4,7,2,6])
predict_y = np.array([(slope*j)+y_intercept for j in predict_x])    
    

plt.figure()
plt.scatter(x, y, color = 'red', label = 'Data Points')
plt.scatter(predict_x, predict_y, color = 'green', label = 'Predicted Ppints')
plt.plot(x, l, color = 'blue', label = 'Regression Line')
plt.legend()
plt.show()   
 
predict_x1 = np.random.normal(3.0, 1.0, 10)
predict_y1 = np.array([(slope*j)+y_intercept for j in predict_x1])   

l1 = regress_line(x1)
plt.figure()
plt.scatter(x1, y1, color = 'red', label = 'Data Points')
plt.scatter(predict_x1, predict_y1, color = 'green', label = 'Predicted Ppints')
plt.plot(x1, l1, color = 'blue', label = 'Regression Line')
plt.legend()
plt.show()
