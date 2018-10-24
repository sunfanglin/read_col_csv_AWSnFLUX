import pandas as pd
#from petl import fromcsv, look, cut, tocsv 
import io
import sys, os
#fn = sys.argv[1]
#path = 'D:/DATA/Naqu/Naqu/'
#path = '/home/sun/naqu_submit/'
path = 'C:/Users/sunfanglin/OneDrive/naqu_submit/'
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
        GRAD_BJ = pd.read_csv(fn, usecols=['Date/Time(BST)', 
                                             'Ta_1.03m_10MinAve', 
                                             'Ta_8.41m_10MinAve',
                                             'RH_1.03m_10MinAve',
                                             'RH_8.41m_10MinAve', 
                                             'WS_0.91m_10MinAve', 
                                             'WS_5.02m_10MinAve',
                                             'WS_10.36m_10MinAve',
                                             'WD_10.36m_10MinAve',
                                             'Pressure_10MinAve',
                                             'Precipitation_10minAcc'])
        GRAD_BJ.to_csv('out/FILD_BOUD_GRAD_MIN30_NAQ'+fn[-9:], encoding='utf-8', index=False)
        SOIL_BJ = pd.read_csv(fn, usecols = ['Date/Time(BST)', 
                                               'Tg_10MinAve', 
                                               'Ts_4cm_10MinAve', 
                                               'Ts_10cm_10MinAve', 
                                               'Ts_20cm_10MinAve', 
                                               'Ts_40cm_10MinAve', 
                                               'SHF_10cm_10MinAve', 
                                               'SHF_20cm_10MinAve', 
                                               'Swc_4cm_10MinAve', 
                                               'Swc_20cm_10MinAve'])
        SOIL_BJ.to_csv('out/FILD_BOUD_SOIL_MIN30_NAQ'+fn[-9:], encoding='utf-8', index=False)
        RADI_BJ = pd.read_csv(fn, usecols= ['Date/Time(BST)',
                                              'Rsd_10MinAve', 
                                              'Rsu_10MinAve', 
                                              'Rld_10MinAve', 
                                              'Rlu_10MinAve'])
        RADI_BJ.to_csv('out/FILD_BOUD_RADM_MIN30_NAQ'+fn[-9:], encoding='utf-8', index=False)

    #########################
    ######  BJ FLUX #########
    #########################

    elif any(c in fn for c in("BJ_Flux","BJ_flux")):
        FLUX_BJ = pd.read_csv(fn, usecols = ['Date/Time', 
                                                'wnd_dir', 
                                                'P_kPa', 
                                                'Avg_T', 
                                                'zoL1', 
                                                'H2', 
                                                'LE2', 
                                                'Fc2', 
                                                'QA_H', 
                                                'QA_LE', 
                                                'QA_Fc'])
        FLUX_BJ.to_csv('out/FILD_BOUD_FLUX_MIN30_NAQ'+fn[-9:], encoding='utf-8', index=False)

    #########################
    ####  Amdo PBL ##########
    #########################

    elif "Amdo_NewPBL" in fn:      ## More observations by PBL since July 2012
        GRAD_AMDO = pd.read_csv(fn, usecols=['Date/Time(BST)',
                                                 'Ta_1.5m_30MinAve',
                                                 'Ta_3m_30MinAve', 
                                                 'Ta_6m_30MinAve', 
                                                 'Ta_12m_30MinAve', 
                                                 'RH_1.5m_30MinAve', 
                                                 'RH_3m_30MinAve', 
                                                 'RH_6m_30MinAve', 
                                                 'RH_12m_30MinAve', 
                                                 'WS_1.5m_30MinAve',
                                                 'WD_1.5m_30MinAve', 
                                                 'WS_3m_30MinAve', 
                                                 'WD_3m_30MinAve', 
                                                 'WS_6m_30MinAve', 
                                                 'WD_6m_30MinAve', 
                                                 'WS_12m_30MinAve', 
                                                 'WD_12m_30MinAve', 
                                                 'Pressure_30MinAve', 
                                                 'Precipitation_30MinAcc'])
        GRAD_AMDO.to_csv('out/FILD_BOUD_GRAD_MIN30_AND'+fn[-9:], encoding='utf-8', index=False)
        SOIL_AMDO = pd.read_csv(fn, usecols = ['Date/Time(BST)',
                                                   'Ts_5cm_30MinAve', 
                                                   'Ts_10cm_30MinAve', 
                                                   'Ts_20cm_30MinAve', 
                                                   'Ts_40cm_30MinAve', 
                                                   'Ts_80cm_30MinAve', 
                                                   'Ts_160cm_30MinAve',
                                                   'SHF_5cm_30MinAve', 
                                                   'SHF_10cm_30MinAve', 
                                                   'Swc_5cm_30MinAve', 
                                                   'Swc_10cm_30MinAve', 
                                                   'Swc_20cm_30MinAve', 
                                                   'Swc_40cm_30MinAve', 
                                                   'Swc_80cm_30MinAve', 
                                                   'Swc_160cm_30MinAve'])
        SOIL_AMDO.to_csv('out/FILD_BOUD_SOIL_MIN30_AND'+fn[-9:], encoding='utf-8', index=False)
        RADI_AMDO = pd.read_csv(fn, usecols= ['Date/Time(BST)',
                                                  'Rsd_30MinAve', 
                                                  'Rsu_30MinAve', 
                                                  'Rld_30MinAve', 
                                                  'Rlu_30MinAve'])
        RADI_AMDO.to_csv('out/FILD_BOUD_RADM_MIN30_AND'+fn[-9:], encoding='utf-8', index=False)

    elif "Amdo_PBL" in fn:           ## Old PBL before July 2012
        GRAD_AMDO = pd.read_csv(fn, usecols=['Date/Time(BST)',
                                                 'Ta_1.53m_30MinAve',
                                                 'Ta_5.56m_30MinAve', 
                                                 'Ta_13.58m_30MinAve', 
                                                 'RH_1.53m_30MinAve', 
                                                 'RH_5.56m_30MinAve', 
                                                 'RH_13.58m_30MinAve', 
                                                 'WS_1.85m_30MinAve',
                                                 'WS_5.96m_30MinAve', 
                                                 'WS_13.89m_30MinAve', 
                                                 'WD_13.89m_30MinAve', 
                                                 'Pressure_30MinAve', 
                                                 'Rain_30Acc'])
        GRAD_AMDO.to_csv('out/FILD_BOUD_GRAD_MIN30_AND'+fn[-9:], encoding='utf-8', index=False)
        SOIL_AMDO = pd.read_csv(fn, usecols = ['Date/Time(BST)',
                                                   'Ts_5cm_30MinAve', 
                                                   'Ts_10cm_30MinAve', 
                                                   'Ts_20cm_30MinAve', 
                                                   'SHF_10cm_30MinAve', 
                                                   'SHF_20cm_30MinAve', ])
        SOIL_AMDO.to_csv('out/FILD_BOUD_SOIL_MIN30_AND'+fn[-9:], encoding='utf-8', index=False)
        RADI_AMDO = pd.read_csv(fn, usecols= ['Date/Time(BST)',
                                                  'Rsd_30MinAve', 
                                                  'Rsu_30MinAve', 
                                                  'Rld_30MinAve', 
                                                  'Rlu_30MinAve'])
        RADI_AMDO.to_csv('out/FILD_BOUD_RADM_MIN30_AND'+fn[-9:], encoding='utf-8', index=False)

    #########################
    ####  Amdo FLUX #########
    #########################

    #elif "Amdo_Flux" in fn:

    elif any(c in fn for c in("Amdo_Flux","Amdo_flux")):
        FLUX_AMDO = pd.read_csv(fn, usecols = ['Date/Time', 
                                                    'wnd_dir', 
                                                    'P_kPa', 
                                                    'Avg_T', 
                                                    'zoL1', 
                                                    'H2', 
                                                    'LE2', 
                                                    'Fc2', 
                                                    'QA_H', 
                                                    'QA_LE', 
                                                    'QA_Fc'])
        FLUX_AMDO.to_csv('out/FILD_BOUD_FLUX_MIN30_AND'+fn[-9:], encoding='utf-8', index=False)
    else :
        print 'filename not match, check file: ', fn

print ' ...Completed! '
