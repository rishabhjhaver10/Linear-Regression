from __future__ import division
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import style
style.use('ggplot')

x = [1,2,3,4,5,6]
y = [6,1,9,5,17,12]

sigma_xi = sum(x)
sigma_yi = sum(y)

def calculate_sigma_xiyi(x, y):
    sigma_xiyi = []
    for i in range(len(x)):
        sigma_xiyi.append(x[i] * y[i])
    return sum(sigma_xiyi)

def calculate_sigma_squared(x):
    sigma_squared = []
    for i in range(len(x)):
        sigma_squared.append(x[i] * x[i])
    return sum(sigma_squared)
    
def calculate_covariance(x, y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean(x)) * (y[i] - mean(y))
    return covar
    
def calculate_variance(x):
    return (calculate_sigma_squared(x) - (sigma_xi ** 2)/len(x))/len(x)

#We will generate some random data first.
x = np.random.normal(3.0, 1.0, 1000)
y = 100 - (x + np.random.normal(0, 0.1, 1000)) * 3

#We define a function that returns slope and intercepts.
def slope_and_intercepts(x, y):
    #y = mx + c
    #Slope(m) = (NΣXY - (ΣX)(ΣY)) / (NΣX2 - (ΣX)2)
    #Intercept(c) = (ΣY - b(ΣX)) / N
    #x and y are the variables.
    #m = The slope of the regression line 
    #c = The intercept point of the regression line and the y axis.	
    #N = Number of observations 
    #ΣXY = Sum of the product of x and y
    #ΣX = Sum of x
    #ΣY = Sum of y
    #ΣX2 = Sum of square x
    slope = (((mean(x)*mean(y)) - mean(x*y)) /
         ((mean(x)*mean(x)) - mean(x*x)))
    
    constant = mean(y) - slope *mean(x)    
    
    print 'The slope is : ' + str(slope)
    print 'The value of constant is : ' + str(constant)
    return slope, constant