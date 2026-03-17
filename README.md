# AQI project

## Goal: To estimate the AQI(PM 2.5) of New Delhi (Safdarjung) using the local climate data, on a day basis.

##       Local climate data: 

```
T	Average Temperature (°C)
TM	Maximum temperature (°C)
Tm	Minimum temperature (°C)
SLP	Atmospheric pressure at sea level (hPa)
H	Average relative humidity (%)
VV	Average visibility (km)
V	Average wind speed (km/h)
VM	Maximum sustained wind speed (km/h)
```

### Software and tool requirement
1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

# Step 1:

Create a new environment for the project
```
conda create -p venv python==3.8 -y
```

Activate it
```
conda activate venv/
```

# Step 2:

Data Collection Part 1: 
```
Downloading HTML pages containing climate data(independent features) for year 2013-2018.
```

Refer file: 
Code - [html_script.py](html_script.py)
Downloaded files - [Data/html_data](Data/html_data)

# Step 3:

Data Collection Part 2: 
```
(AQI data already downloaded in system: Each file provides hourly AQI data for a year)
Extracting average AQI for each day of the year and plotting AQI over 2013, 2014 and 2015.
```

Refer file: 
Code - [plot_AQI.py](plot_AQI.py)
Downloaded files - [Data/AQI](Data/AQI)

# Step 4:

Data Collection Part 3: 
```
Combining the data collected from HTML files (independent variables) and AQI files (dependent variable) to create a new csv file containing all the features for each day of the year.
```

Refer file: 
Code - [extract_combine.py](extract_combine.py)
Downloaded files - [Data/real_data](Data/real_data)

# Step 4:

Apply ML algorithms:
```
Linear Regression
Lasso Regression
Decision Tree Regressor
KNN Regressor
RandomForestRegressor
Xgboost Regressor
ANN-Artificial Neural Network
```
In each file, following steps are done:
```
Feature engineering:
1. Handling missing values.
2. Seperating independent and dependent values.
3. Checking datatypes (categorical/numerical).
4. Analysing correlation.
5. Checking feature importance.
6. Observing distribution of target variable.
Model building:
1. Train test split.
2. Training the model on train set.
3. Checking R2 score.
4. Performing cross validation.
5. Predicting on test set.
6. Plotting histogram and scatter plot of residuals.
7. Checking performance metrics: Mean absolute error, mean squared error, root mean squared error.
8. Dumping trained model in a pickle file.
```

Refer file:
[LinearRegression](LinearRegression.ipynb)
[LassoRegression](LassoRegression.ipynb)
[DecisionTreeRegressor](DecisionTreeRegressor.ipynb)
[KNearestNeighborRegressor](KNearestNeighborRegressor.ipynb)
[RandomForestRegressor](RandomForestRegressor.ipynb)
[xgboostregressor](xgboostregressor.ipynb)
[ANN](ANN.ipynb)