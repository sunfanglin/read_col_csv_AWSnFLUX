
import pandas as pd
#from petl import fromcsv, look, cut, tocsv 
import io
import sys, os
import datetime
import numpy as np
#fn = sys.argv[1]
#path = 'D:/DATA/Naqu/Naqu/'
path = '/home/sun/naqu_submit/data/'
outpath = '/home/sun/naqu_submit/fillmissing/'
print "\n ********************\n The input files are in ", path, "\n"
#path = 'C:/Users/Fanglin/OneDrive/naqu_submit/'
#path = 'D:/DATA/QOMSAWS/'
files = [f for f in os.listdir(path) if f.endswith(('.csv'))]
print 'Data files are: \n' , files
#f_out1=open(path+'SS_data_15-17.txt', 'a')
for fn in files:
    print fn
    #os.system('sed -i '+"'1s/ //g' "+fn)     ## remove empty spaces in first line of input file, used when reporting error of not existing headers

    #########################
    ######  BJ AWS  #########
    #########################
    if "BJ_AWS" in fn:
        dt = datetime.timedelta(minutes = 10)    # change 10 min to time 
        fill_list = (np.nan*np.ones(29)).tolist()     # a list consits of 121 "-999.9"s
        fillvalue = ','.join(str(x).upper() for x in fill_list)+'\n'  # change list to string, seperated with Tab
        fin = open(path+fn, 'r')
        fout = open(outpath+fn[:-4]+'.csv', 'a')
        lines = fin.readlines()
        fout.write(lines[0])
        fout.write(lines[1])
        #time_col = pd.read_csv(fn, usecols=['Date/Time(BST)'])
        #print time_col[0,0]
        #raw_input()
        count = 0
        for i in range(1, len(lines)-1):
            timestr0 = lines[i].split(',')[0]
            timestr1 = lines[i+1].split(',')[0]
            ts0 = datetime.datetime.strptime(timestr0, "%Y-%m-%d %H:%M:%S")
            ts1 = datetime.datetime.strptime(timestr1, "%Y-%m-%d %H:%M:%S")
            while (ts1 - ts0) > dt :   # dt is 10 min
                ts0 = ts0 + dt
                timestamp = datetime.datetime.strftime(ts0, "%Y-%m-%d %H:%M:%S") # Change time 
                fout.write(timestamp+',' + fillvalue)
                count = count +1
                #fout.write(timestamp + '\tQOMOLANGMA\t'+fillvalue)
            fout.write(lines[i+1])
        fin.close()
        fout.close()
        print count, 'records missed!'

    if "Amdo_PBL" in fn:
        dt = datetime.timedelta(minutes = 30)    # change 10 min to time 
        fill_list = (np.nan*np.ones(26)).tolist()     # a list consits of 121 "-999.9"s
        fillvalue = ','.join(str(x).upper() for x in fill_list)+'\n'  # change list to string, seperated with Tab
        fin = open(path+fn, 'r')
        fout = open(outpath+fn[:-4]+'.csv', 'a')
        lines = fin.readlines()
        fout.write(lines[0])
        fout.write(lines[1])
        #time_col = pd.read_csv(fn, usecols=['Date/Time(BST)'])
        #print time_col[0,0]
        #raw_input()
        count = 0
        for i in range(1, len(lines)-1):
            timestr0 = lines[i].split(',')[0]
            timestr1 = lines[i+1].split(',')[0]
            ts0 = datetime.datetime.strptime(timestr0, "%Y-%m-%d %H:%M:%S")
            ts1 = datetime.datetime.strptime(timestr1, "%Y-%m-%d %H:%M:%S")
            while (ts1 - ts0) > dt :   # dt is 10 min
                ts0 = ts0 + dt
                timestamp = datetime.datetime.strftime(ts0, "%Y-%m-%d %H:%M:%S") # Change time 
                fout.write(timestamp+',' + fillvalue)
                count = count +1
                #fout.write(timestamp + '\tQOMOLANGMA\t'+fillvalue)
            fout.write(lines[i+1])
        fin.close()
        fout.close()
        print count, 'records missed!'

    if "Amdo_NewPBL" in fn:
        dt = datetime.timedelta(minutes = 30)    # change 10 min to time 
        fill_list = (np.nan*np.ones(50)).tolist()     # a list consits of 121 "-999.9"s
        fillvalue = ','.join(str(x).upper() for x in fill_list)+'\n'  # change list to string, seperated with Tab
        fin = open(path+fn, 'r')
        fout = open(outpath+fn[:-4]+'.csv', 'a')
        lines = fin.readlines()
        fout.write(lines[0])
        fout.write(lines[1])
        #time_col = pd.read_csv(fn, usecols=['Date/Time(BST)'])
        #print time_col[0,0]
        #raw_input()
        count = 0
        for i in range(1, len(lines)-1):
            timestr0 = lines[i].split(',')[0]
            timestr1 = lines[i+1].split(',')[0]
            ts0 = datetime.datetime.strptime(timestr0, "%Y-%m-%d %H:%M:%S")
            ts1 = datetime.datetime.strptime(timestr1, "%Y-%m-%d %H:%M:%S")
            while (ts1 - ts0) > dt :   # dt is 10 min
                ts0 = ts0 + dt
                timestamp = datetime.datetime.strftime(ts0, "%Y-%m-%d %H:%M:%S") # Change time 
                fout.write(timestamp+',' + fillvalue)
                count = count +1
                #fout.write(timestamp + '\tQOMOLANGMA\t'+fillvalue)
            fout.write(lines[i+1])
        fin.close()
        fout.close()
        print count, 'records missed!'
    if any(c in fn for c in ("Flux", "flux")):
        dt = datetime.timedelta(minutes = 30)    # change 10 min to time 
        fill_list = (np.nan*np.ones(22)).tolist()     # a list consits of 121 "-999.9"s
        fillvalue = ','.join(str(x).upper() for x in fill_list)+'\n'  # change list to string, seperated with Tab
        fin = open(path+fn, 'r')
        fout = open(outpath+fn[:-4]+'.csv', 'a')
        lines = fin.readlines()
        fout.write(lines[0])
        fout.write(lines[1])
        #time_col = pd.read_csv(fn, usecols=['Date/Time(BST)'])
        #print time_col[0,0]
        #raw_input()
        count = 0
        for i in range(1, len(lines)-1):
            timestr0 = lines[i].split(',')[0]
            timestr1 = lines[i+1].split(',')[0]
            ts0 = datetime.datetime.strptime(timestr0, "%Y-%m-%d %H:%M")
            ts1 = datetime.datetime.strptime(timestr1, "%Y-%m-%d %H:%M")
            while (ts1 - ts0) > dt :   # dt is 10 min
                ts0 = ts0 + dt
                timestamp = datetime.datetime.strftime(ts0, "%Y-%m-%d %H:%M") # Change time 
                fout.write(timestamp+',' + fillvalue)
                count = count +1
                #fout.write(timestamp + '\tQOMOLANGMA\t'+fillvalue)
            fout.write(lines[i+1])
        fin.close()
        fout.close()
        print count, 'records missed!'
print "\n***************************************\n...... Complete! Check output files in ", outpath
      

