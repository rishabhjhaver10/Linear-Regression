#This code has its inspiration from Data Science and Machine Learning with Python course by Frank Kane on www.udemy.com.

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

#Model 1
#Generating page speeds randomly with a mean of 3, standard deviation of 0.5 and for 1000 people.
page_speeds = np.random.normal(3, 0.5, 1000)
#Generating amount spent by customer randomly with a mean of 70, standard deviation of 5 and for 1000 people.
amount_spent = np.random.normal(70, 5, 1000)
#Plotting a scatter plot of page speeds vs amount spent by customer
plt.figure(1)
plt.scatter(page_speeds, amount_spent)
plt.title('Model 1')
plt.xlabel('Time taken to load a page')
plt.ylabel('Amount spent by customer')
#Performing linear regression
#Model: y = m*x + c : amount spent by customer = slope * page speeds + constant
slope, intercept, r_value, p_value, std_err = stats.linregress(page_speeds, amount_spent)
fit_line = predict(page_speeds)
plt.plot(page_speeds, fit_line, c = 'r')
plt.show()
print 'The value of r-squared is : ' + str(r_value ** 2)
good_fit(r_value)

#As we can see from the value of r-squared that if we fit a line it might not be a very good fit.
#Because the data is randomly generated and we do not have a linear relationship between variables.
#Now we build another model in which we will explicitly give a linear relationship between variables.

#Model 2
page_speeds_1 = np.random.normal(3, 0.5, 1000)
#For this model we have explicitly given a linear relationship.
amount_spent_1 = 100 - (page_speeds_1 + np.random.normal(0, 0.1, 1000)) * 1.5
plt.figure(2)
plt.scatter(page_speeds_1, amount_spent_1)
plt.title('Model 2')
plt.xlabel('Time taken to load a page')
plt.ylabel('Amount spent by customer')
slope, intercept, r_value, p_value, std_err = stats.linregress(page_speeds_1, amount_spent_1)   
fit_line1 = predict(page_speeds_1)
plt.plot(page_speeds_1, fit_line1, c = 'r')
plt.show()
print 'The value of r-squared is : ' + str(r_value ** 2)
good_fit(r_value)


#We define a function to fit the line.
def predict(x):
    return slope * x + intercept

#We define a function to display if it a good fit or not.
def good_fit(x):
    y = x * x
    if y > 0.5:
        print 'It is a good fit'
    else:
        print 'It is not a good fit'