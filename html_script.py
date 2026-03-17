## Data collection part 1
## Extracting data from HTML pages

import os
import time
import requests
## requests is a library for making HTTP requests in Python. 
## It allows you to send HTTP requests and handle responses easily.
import sys



def retreive_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if (month < 10):
                ## Climate New Delhi / Safdarjung
                url= f"https://en.tutiempo.net/climate/0{month}-{year}/ws-421820.html"
            else:
                url= f"https://en.tutiempo.net/climate/{month}-{year}/ws-421820.html"
                
                
            ## Fetching the url content using requests.get() method.                 
            texts = requests.get(url)
                
            ## Encoding the text content of the response to UTF-8 format. 
            text_utf= texts.text.encode('utf=8')
            
            ## Make a directory for year if it does not exist    
            if not os.path.exists(f"Data/html_data/{year}"):
                os.makedirs(f"Data/html_data/{year}")
            
            ## within year directory    
            with open(f"Data/html_data/{year}/{month}.html","wb") as output:
                output.write(text_utf)
                
        ## Printing the progress of the data collection process.
        sys.stdout.flush()
            
            
if __name__ == "__main__":
    start_time = time.time()
    retreive_html()
    stop_time = time.time()
    print(f"Data collection completed in {stop_time - start_time} seconds.")
                
                
                
                

                
