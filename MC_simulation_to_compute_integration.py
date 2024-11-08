#import the necessary packages

import random
import numpy as np
import math

# Define the function
def f(x):
    return (np.log(x)/x)  

#set the number of samples you want to take
N = 1000000

#Initialize the counter for points inside the graph lnx/x
inside = 0

#Set the limit of x and y
x_min, x_max = 1, 20
y_min, y_max = 0, 1

#Calculate the area inclosed by x and y
area_inclosed = (x_max-x_min)*(y_max-y_min)

for i in range(N):
    #Generate random number
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)

    #Check if the point is inside the area
    if y <= f(x):
        inside+= 1
        
#Estimate the integral
integral_value = (inside/N)*area_inclosed

#print the final value
print("Estimated integral of ln(x)/x from 1 to 10 is: ", integral_value) 