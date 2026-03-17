
## Data collection part 3
## In this part we combine the data collected from HTML files (independent variables) 
# and csv files (dependent variable) to create a 
# new csv file containing all the features for each day of the year.

## importing functions from plot_AQI.py to get the average AQI values for each day of the year.
from plot_AQI import avg_data_2013,avg_data_2014,avg_data_2015,avg_data_2016

import pandas as pd
import requests
import sys

## to extract data from html files, use beautifulsoup library
from bs4 import BeautifulSoup

import os
import csv

## Extract html data from the dowloaded html files for each month of each year.
def met_data(month,year):
    
    ## reading html file
    file_html = open(f"Data/html_data/{year}/{month}.html", "rb")
    plain_text = file_html.read()
    
    tempD = []
    
    ## getting the data from the html file using BeautifulSoup library. 
    ## getting the text content of the html file for every row,
    ## each row containing 15 text content (15 features)
    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.find_all('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)
                ## Now you have a list of all the text contents
                ## (Feature contents) for a year.
                
    ## getting number of rows
    rows = len(tempD) / 15
    
    
    ## creating a list of lists, where each inner list contains the 15 features for a particular row.
    finalD = []
    
    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)
    
    length = len(finalD)
    ## Now we have a list of lists, where each inner list contains features for a day.
    
    finalD.pop(length-1)
    finalD.pop(0)
    ## removed the first and last row as they contain unwanted data.
    
    ## Remove the unwanted features/columns
    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)
        
    return finalD


## converting data from real_data files into list of lists.
def data_combine(year, cs):
    for a in pd.read_csv(f"Data/real_data/real_{year}.csv",chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
        return mylist


## Here combine html data and AQI data to create a 
# new csv file containing all the features for each day of the year.
if __name__ == "__main__":
    
    ## making real_data directory
    if not os.path.exists("Data/real_data"):
        os.makedirs("Data/real_data")
    
    for year in range(2013,2017):
        
        ## Create a excel file for each year to store the combined data of that year.
        with open(f"Data/real_data/real_{year}.csv", "w") as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(["T",'TM','Tm','SLP','H','VV','V','VM','PM2.5'])
            
        final_data = []
        
        ## Fetch monthly data for independent features and
        ## combine them to get the data for the whole year.
        for month in range(1,13):
            temp = met_data(month,year)
            final_data = final_data + temp
            
        ## Fetch the average AQI values (dependent features) for each day of the year 
        ## using the functions defined in plot_AQI.py
        pm = getattr(sys.modules[__name__], f"avg_data_{year}")()
        
        if len(pm) == 364:
            pm.insert(364,'-')
            
        ## Combine the independent features and dependent features 
        ## to create a new list of lists,
        for i in range(len(final_data)-1):
            final_data[i].insert(8,pm[i])
            
        ## write file with the rows from final_data list,
        ## while handling any missing values appropriately.
        with open(f"Data/real_data/real_{year}.csv", "a") as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == '' or elem == '-':
                        flag = 1
                if flag != 1:
                    wr.writerow(row)
                    ## finally we have the combined data for each year in a separate csv file.
    
    
    
    
    
    ## fetch the list converted data from csv files for each year 
    ## using data_combine function defined above.    
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
    
    ## Combine the data for all years into a single list of lists,
    total_data = data_2013 + data_2014 + data_2015 + data_2016
    
    with open(f"Data/real_data/real_combine.csv", "w") as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(["T",'TM','Tm','SLP','H','VV','V','VM','PM2.5'])
        wr.writerows(total_data)