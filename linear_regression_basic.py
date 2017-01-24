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