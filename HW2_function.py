# Homework2, 09-19-2013
# Samira Ardani

####################################################################################################################
# This function reads the URL address for the USGS website and returns the discharge for particular duration of time 
# Inputs are: station number, start date and end date
# Outputs are: The discharge for particular duration of time that we entered as input in the function and the dates

# HW2_function('02476500',2010,12,1,2013,8,1)
#####################################################################################################################
    
import urllib 
from datetime import datetime
import numpy as np
#import matplotlib.pyplot as plt

def HW2_function(station_no,start_y,start_m,start_d,end_y,end_m,end_d):
    
    '''
    HW2_function reads the USGS website using the URL.The first input is the station number. 
    The next three inputs are the year, months and day of starting date and the last three inputs are those of end date.
    The outputs are the dates and discharge respectively for that time interval.
      
    '''
    url = []
    start_date = str(datetime(start_y,start_m,start_d).date())
    end_date   = str(datetime(end_y,end_m,end_d).date())
     
    url = 'http://nwis.waterdata.usgs.gov/ms/nwis/uv?cb_00065=on&cb_00060=on&format=rdb&period=&begin_date='+start_date+'&end_date='+end_date+'&site_no='+station_no

    data = urllib.urlopen(url)
    
    discharge   = []
    dates       = []

    for line in data.readlines()[29:]:
        data_line = line.split()
        discharge.append(float(data_line[5]))
        date   = data_line[2]
        time   = data_line[3]
        year   = int(date.split('-')[0])
        month  = int(date.split('-')[1])
        day    = int(date.split('-')[2])
        hour   = int(time.split(':')[0])
        minute = int(time.split(':')[1])
        dates.append(datetime(year,month, day,hour,minute))

    discharge = np.array(discharge) 
    dates = np.array(dates)
      
    #plt.figure()
    #plt.plot(discharge) 
    #plt.ylabel('discharge')
    #plt.show()   
        
          
    return dates, discharge
    
      
    
