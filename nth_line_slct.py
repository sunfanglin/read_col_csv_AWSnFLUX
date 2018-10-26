
import pandas as pd
import csv
#from petl import fromcsv, look, cut, tocsv 
import io
import sys, os
import datetime
import numpy as np
#fn = sys.argv[1]
path = '/home/sun/naqu_submit/null/'
outpath = '/home/sun/naqu_submit/30min/'
outpath2 = '/home/sun/naqu_submit/60min/'
print "\n ********************\n Input path: ", path, "\n"
files = [f for f in os.listdir(path) if f.endswith(('.csv'))]


#######################
#### 30 min ##########
########################
print "\n ********************\n Generating 30-min data ... \n"

for fn in files:
    print fn
    #########################
    ######  BJ AWS  #########
    #########################
    if "BJ_AWS" in fn:
        with open(path+fn) as infile:
            with open(outpath+fn, 'w') as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames = reader.fieldnames)
                writer.writeheader()
                # iterate through file and write only every 5th row
                writer.writerows([x for i,x in enumerate(reader) if i % 3 == 0])
    else:
        with open(path+fn) as infile:
            with open(outpath+fn, 'w') as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames = reader.fieldnames)
                writer.writeheader()
                # iterate through file and write only every 5th row
                writer.writerows([x for i,x in enumerate(reader) if i % 1 == 0])

#######################
#### 60 min ##########
########################

print "\n ********************\n Generating 60-min data ... \n"
for fn in files:
    print fn
    #########################
    ######  BJ AWS  #########
    #########################
    if "BJ_AWS" in fn:
        with open(path+fn) as infile:
            with open(outpath2+fn, 'w') as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames = reader.fieldnames)
                writer.writeheader()
                # iterate through file and write only every 5th row
                writer.writerows([x for i,x in enumerate(reader) if i % 6 == 0])
    else:
        with open(path+fn) as infile:
            with open(outpath2+fn, 'w') as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames = reader.fieldnames)
                writer.writeheader()
                # iterate through file and write only every 5th row
                writer.writerows([x for i,x in enumerate(reader) if i % 2 == 0])
print "\n***************************************\n...... Complete! Check output files in ", outpath
print " and ", outpath2




