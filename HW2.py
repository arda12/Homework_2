# Homework2, 09-19-2013
# Samira Ardani

# This script calculates the mean and standard deviation of annual discharge for USGS historical data set.
# first, HW2_function is used to costruct the URL, time data and discharge array for an arbitrary start date, end date and station number.
# Then, the timeseries is analysed according to this script to calculate the annual mean and standard deviation of discharge. The plot shows the result of this analysis
# We use the data for station no: 01100000 for start date 1931-1-1 and end date 2013-1-1

####################################################################################################################

import HW2_function as function
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

foo = function. HW2_function('01100000',1931,1,1,2013,1,1)

time = foo[0]
discharge = foo[1]

months = np.array([time[t].month for t in range(time.size)])
days   = np.array([time[t].day for t in range(time.size)])
years  = np.array([time[t].year for t in range(time.size)])

mean   = []
std    = []
           
for i in range(1,13):     
    idx   = np.where (months ==i)
    d_ave = discharge[idx]
    
    for j in range (1,32):
        iidx          = np.where(days[idx]==j)
        discharge_ave = d_ave[iidx]
        
        #print discharge_ave
        mean.append(discharge_ave.mean())
        std.append(discharge_ave.std())        

mean = np.array(mean)
std  = np.array(std)
mean = mean[~np.isnan(mean)]
std  =  std[~np.isnan(std)]

up_limit   = mean+std
down_limit = mean-std

# plotting the discharge time series:
# In this part, program takes the interval that you want to plot. 
# time_data: is a time array for 2012 with 366 days chosen as a reference year for 
#corresponding mean and standard deviation array.
#The plotting interval must be inside the total timeseries not beyond that (In here it is between 01-01-1931 and 01-01-2013)    

start_time = datetime(2010,1,1)
end_time   = datetime(2013,1,1)
idx_start  = np.where(time==start_time)
idx_end    = np.where(time==end_time)
time_data  = time[np.where(years==2012)]

select_discharge = np.array([discharge[d] for d in range(idx_start[0],idx_end[0])])
 
total_mean       =[]
total_up_limit   =[]
total_down_limit =[]
for t in time[idx_start[0]:idx_end[0]]:
    total_mean.append(mean[time_data==datetime(2012,t.month,t.day)])
    total_up_limit.append(up_limit[time_data==datetime(2012,t.month,t.day)])
    total_down_limit.append(down_limit[time_data==datetime(2012,t.month,t.day)])  
    
          
fig = plt.figure()
plt.plot(time[idx_start[0]:idx_end[0]],select_discharge,"m",linewidth=0.25,label = 'timeseries')
plt.plot(time[idx_start[0]:idx_end[0]],total_mean,label='mean')
plt.plot(time[idx_start[0]:idx_end[0]],total_up_limit,"-.r",label = 'standard deviation')
plt.plot(time[idx_start[0]:idx_end[0]],total_down_limit,"-.r")
plt.title('Annual Mean and Standard Deviation for Discharge', fontsize =16 , style ='italic' )
plt.xlabel('Time (s)',fontsize = 15, style = 'italic') 
plt.ylabel('Discharge ($ft^3/s$)',fontsize = 15, style = 'italic')
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.2,left=0.2)
plt.legend(loc = 'upper right')
plt.show()
plt.savefig('timeseries.png')
