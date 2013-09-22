# Homework2, 09-19-2013
# Samira Ardani

####################################################################################################################

import HW2_function as function
import matplotlib.pyplot as plt

foo = function. HW2_function('02476500',2009,5,1,2009,6,1)

foo[1]
foo[1].mean
print 'Mean discharge for this period is:', foo[1].mean()

foo[1].max
print 'Max discharge for this period is:', foo[1].max()

foo[1].min
print 'Min discharge for this period is:', foo[1].min()

# plotting the discharge time series:
plt.figure()
plt.plot(foo[0],foo[1])
plt.xlabel('time') 
plt.ylabel('discharge, ft^3/s')
plt.show() 
