import urllib 
from datetime import datetime
import numpy as np

url = 'http://nwis.waterdata.usgs.gov/ms/nwis/uv?cb_00065=on&cb_00060=on&format=rdb&period=&begin_date=2012-09-12&end_date=2013-09-19&site_no=02476500'

#    url.split('&')[4].split('=')[1]
#    url.split('&')[5].split('=')[1]
 #   new_url = url.replace(url.split('&')[4].split('=')[1],
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

discharge = np.array( discharge) 
date = np.array(dates)