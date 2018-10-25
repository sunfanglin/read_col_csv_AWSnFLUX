
import pandas as pd
import xlrd
import time
#from petl import fromcsv, look, cut, tocsv 
import io
import sys, os
#fn = sys.argv[1]
#path = 'C:/Users/sunfanglin/OneDrive/naqu_submit/'
path = '/home/sun/naqu_submit/data/'
#path = 'D:/DATA/QOMSAWS/'
files = [f for f in os.listdir(path) if f.endswith(('.xls'))]
#f_out1=open(path+'SS_data_15-17.txt', 'a')
for fn in files:
    print fn, '==>',
    data = pd.read_excel(path+fn)
    data.to_csv(path+fn[:-4]+'.csv',encoding='utf-8',index=None)
    print fn[:-4]+'.csv'
    time.sleep(1.2)
    
    

