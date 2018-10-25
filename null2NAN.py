import pandas as pd
import io
import sys, os
import datetime
import numpy as np
#fn = sys.argv[1]
#path = 'D:/DATA/Naqu/Naqu/'
path = '/home/sun/naqu_submit/fillmissing/'
outpath = '/home/sun/naqu_submit/null/'
print "\n ********************\n The input files are in ", path, "\n"
#Read the csv into a Pandas DataFrame
files = [f for f in os.listdir(path) if f.endswith(('.csv'))]
for fn in files:
    print fn
    flights = pd.read_csv(path+fn,low_memory=False)
    #Examine the shape of the data
#    flights.shape
    #Explore null cells
 #   flights.isnull()
    #View total of null values by column
  #  flights.isnull().sum()
    #View the number of null values in the 'TAXI_OUT' column
    #flights['TAXI_OUT'].isnull().sum()
    #Fill all null values with a space, and score that in the current data frame
    flights=flights.fillna("NAN")
    #Store the dataframe as a new CSV
    flights.to_csv(outpath+fn, index=False)
print "\n***************************************\n...... Complete! Check output files in ", outpath
