## Data collection part 2
## In HTML data there are only independent variables. 
## Here we have already downloaded files containing the dependent variable (PM2.5) in csv format,
## which contains AQI data for every hour over a span of a year.

import pandas as pd
import matplotlib.pyplot as plt

def avg_data_2013():
    temp_i=0
    average=[]
    
    ## To find out average value of AQI for each day, 
    ## we read the csv file in chunks of 24 rows (24 hours in a day).
    ## This is done because in html_data, we have data for each day.
    for rows in pd.read_csv("Data/AQI/aqi2013.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        
        ## We create a dataframe for each chunk of 24 rows 
        df=pd.DataFrame(data=rows)
        
        ## Iterate through each row to extract the PM2.5 values.
        for index,row in df.iterrows():
            data.append(row["PM2.5"])
            
        ## Iterate through each PM2.5 value to calculate the sum for the day, 
        ## while handling any non-numeric values appropriately.
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var+temp
                    
        ## Calculate avg for each day
        avg = add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
        ## Now we have the list 'average' which contains 
        ## the average AQI for each day of the year 2013.
    return average
    
## Similarly do it for other years as well.


def avg_data_2014():
    temp_i=0
    average=[]
    
    for rows in pd.read_csv("Data/AQI/aqi2014.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row["PM2.5"])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var+temp
                    
        avg = add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average

def avg_data_2015():
    temp_i=0
    average=[]
    
    for rows in pd.read_csv("Data/AQI/aqi2015.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row["PM2.5"])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var+temp
                    
        avg = add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average

def avg_data_2016():
    temp_i=0
    average=[]
    
    for rows in pd.read_csv("Data/AQI/aqi2016.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row["PM2.5"])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var+temp
                    
        avg = add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average

def avg_data_2017():
    temp_i=0
    average=[]
    
    for rows in pd.read_csv("Data/AQI/aqi2017.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row["PM2.5"])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var+temp
                    
        avg = add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average

def avg_data_2018():
    temp_i=0
    average=[]
    
    for rows in pd.read_csv("Data/AQI/aqi2018.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row["PM2.5"])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var+temp
                    
        avg = add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average



## plotting the average AQI values for each day of the year for 2013, 2014 and 2015 to visualize the trend of AQI over the years.
if __name__ == "__main__": 
    lst2013=avg_data_2013()
    lst2014=avg_data_2014()
    lst2015=avg_data_2015()
    lst2016=avg_data_2016()
    lst2017=avg_data_2017()
    lst2018=avg_data_2018()
    plt.plot(range(0,365),lst2013,label="2013")
    plt.plot(range(0,364),lst2014,label="2014")
    plt.plot(range(0,365),lst2015,label="2015")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()