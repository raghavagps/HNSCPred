import os
import pandas as pd
import tensorflow 
from tensorflow import keras

def predict(df):

    # Removing all the cells with zero values in it.i.e. all the rows have zero in it.

    df= df.loc[(df!=0).any(axis=1)]

    #df1 = df.loc[:,(df==0).mean()<0.8] ## removing all the columns with more than 80 % zeroes 

    selected_genes = ['PLAC9', 'UBB', 'ACKR1', 'AQP7', 'FXYD1', 'BTG1', 'B2M', 'CFD', 'LTBP4',
       'RPS11', 'MFAP4', 'ISG20', 'SARAF', 'RPL28', 'ABCA8', 'YPEL5', 'GSN',
       'IL2RG', 'OAZ1', 'DPT', 'RPLP1', 'TNXB', 'CD37', 'ARPC3', 'CYBRD1',
       'SDPR', 'RELB', 'CYBA', 'TIMP3', 'RPS19', 'CREM', 'NOVA1', 'RPS26',
       'PDGFRL', 'HLA-C', 'CXCL12', 'TGFBR3', 'RAC2', 'SERP1', 'VIT', 'RHOG',
       'ADH1B', 'RHOH', 'COPE', 'DCN', 'CNN2', 'REL', 'CD34', 'OST4', 'PRELP',
       'EPSTI1', 'PTGIS', 'SOD3', 'TNIP1', 'LIMD2', 'RPS15A', 'DUSP4',
       'SPARCL1', 'SCARA5', 'HLA-B', 'FBLN2', 'IDH2', 'ANGPTL1', 'HLA-A',
       'FHL1', 'EZR', 'GPSM3', 'F10', 'EEF1A1', 'CYTIP', 'FBLN5', 'CIB1',
       'CXCR4', 'ATP5E', 'FIGF', 'PLPP3', 'PIM3', 'PSME1', 'CILP', 'CD7',
       'EBF1', 'NDUFB11', 'ICAM3', 'MGP', 'SLC16A3', 'MEG3', 'VOPP1', 'TXNIP',
       'RPS15', 'SSPN', 'UBC', 'BMP4', 'TIGIT', 'ADAR', 'LRRN4CL', 'SUB1',
       'GDF10', 'WIPF1', 'ABI3BP', 'FAM177A1']      
    df1 = df[selected_genes]


    # Load the model

    dir_location = os.path.join(os.path.dirname(__file__), 'hnscc')

    #Load model
    model = keras.models.load_model(dir_location)



    y_pred = model.predict(df1)

    predictions = list(map(lambda x: 0 if x<0.5 else 1, y_pred))

    ones = 0
    zeros =0

    for i in range(len(predictions)):
      if (predictions[i]==1):
          ones +=1
      else:
          zeros+=1

    #print("The number of ones are ", ones)
    #print("The number of zeros are ", zeros)
    #print("Total number of cells are ", len(predictions))
    #print("Predicted percentage of Diseased cells are ", ones/len(predictions))
    #print("Predicted percentage of Normal cells are ", zeros/len(predictions))

    op= ones/len(predictions) 
    zp= zeros/len(predictions)

    if(op>0.6):
      print("HNSCC patient detected, {} percentage diseased cells detected".format(op*100))
      # Load the model
      selected_genes1 = ['LGALS1','REL','PKIA','MAGEA4','HSPA6','XIST','IGKV1-39','A2ML1','IFITM3','ZFR2','TREM1','ABL2','HSPH1','KRT19','SAT2','EMP3','EPHX3','PLCG2','PMP22','CD44','HSPA1A','TMEM98','SYCP2','NFKB1','FTH1','PIK3IP1','C4orf48','KIAA1211L','SELM','TRAT1','IGHV5-51','RP11-160E2.6','SMIM22','IER3','IGF2BP2','EGLN3','CD63','SMC1B','MIR22HG','BCL2A1','MMP14','CH17-262H11.1','SULT2B1','SLC7A11','DNAJB1','B2M','KDM6B','PTK7','TMC8','S100A4','SOD2','SULF2','CSTB','CYBA','KLHL35','PRKCDBP','GRAMD1A','DNAJA4','EREG','ASTN2','KLF6','FLNA','TIMP1','SUSD4','S100A6','TIMP2','ANXA5','PRSS8','FAM159A','PTGS1','SYNGR3','MFAP2','LINC00936','STAG3','FOSL2','FHAD1','PPFIA1','FSTL1','IGHV4-59','LMNA','CALML5','SERPINB9','NRP1','CD8B','MT-ND5','SCNN1B','CXCL2','RPS4Y1','ANPEP','MALAT1','TMEM256','IGHV3-73','C1S','CLDN10','GRINA','PTGS2','RP11-173C1.1','COL12A1','RHCG','MS4A1']

      df2 = df[selected_genes1]


      dir_location1 = os.path.join(os.path.dirname(__file__), 'hpv')

      #Load model
      model1 = keras.models.load_model(dir_location1)
      y_pred1 = model1.predict(df2)

      predictions1 = list(map(lambda x: 0 if x<0.5 else 1, y_pred1))

      ones1 = 0
      zeros1 =0

      for i in range(len(predictions1)):
          if (predictions1[i]==1):
              ones1 +=1
          else:
              zeros1+=1

      #print("The number of ones are ", ones)
      #print("The number of zeros are ", zeros)
      #print("Total number of cells are ", len(predictions))
      #print("Predicted percentage of Diseased cells are ", ones1/len(predictions1))
      #print("Predicted percentage of Normal cells are ", zeros1/len(predictions1))

      op1= ones1/len(predictions1) 
      zp1= zeros1/len(predictions1)
      if(op1>0.8):
            print("HNSCC HPV- patient detected, {} percentage HPV- cells classified".format(op1*100))
      else: 
            print("HNSCC HPV+ patient detected, {} percentage HPV+ cells classified".format(zp1*100))
    else:
      print("Normal patient detected, {} percentage normal cells detected".format(zp*100))
