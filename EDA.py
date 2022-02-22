#import libraries
from numpy import sort #this appeared on its own
import pandas as pd
import csv #added this to try to get code to run, don't know if it helped
import matplotlib.pyplot as plt

#read in the data
df = pd.read_csv('NFLX.csv')

#let's see the dataset
df.head(4)

#EDA 
df.dtypes
df.describe()

#this dataset covers Netflix stock prices at open and close
#what is the date range for this dataset?

#look at the date column only
df['Date'].head()

#to find range of years, find the beginning and end of this date column
df['Date'].min() #this resulted in 05/23/2002
df['Date'].max() #this resulted in 01/11/2022

#this data is ~20 years of Netflix stock prices (!!)

df.info #4945 rows, 7 columns

#trying to successfully use matplotlib 

df.plot(kind= 'scatter',x='Date', y='High')
plt.title('scatterplot')
plt.show()