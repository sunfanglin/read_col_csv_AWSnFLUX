
import pandas as pd
import xlrd
#from petl import fromcsv, look, cut, tocsv 
import io
import sys, os
#fn = sys.argv[1]
path = '/home/sun/naqu_submit/'
#path = 'D:/DATA/QOMSAWS/'
files = [f for f in os.listdir(path) if f.endswith(('.xls'))]
#f_out1=open(path+'SS_data_15-17.txt', 'a')
for fn in files:
    print fn, '==>',
    data = pd.read_excel(fn)
    data.to_csv(fn[:-4]+'.csv',encoding='utf-8')
    print fn[:-4]+'.csv'
    
    

