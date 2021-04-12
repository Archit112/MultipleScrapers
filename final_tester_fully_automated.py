# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:53:42 2020

@author: archi
"""


import itertools
import pandas as pd  
from datetime import date
import datetime
import os
import time


start_time = time.time()

dnt = str(datetime.datetime.today().strftime('%d'))
dnt='30'
dt = str(datetime.datetime.today().strftime('%d-%m-%Y'))
dt='30-11-2020'
mnth = str(datetime.datetime.strptime(dt, "%d-%m-%Y").month)
mnth='11'

if dnt=='01':
    files = os.listdir("E:\\Naaniz Internship\\DMART_UPDATE_ID\\Data")
    #print("HERE")
    today_date=dnt
    transcripts_d1=[]
    for l in files:
        #print(i)
        dt_now = str(l[0])+str(l[1])
        if dt_now == today_date:
            #print("Check")
            file1 = "E:/Naaniz Internship/DMART_UPDATE_ID/Data/"+l
            #print(file1)
            df_1 = pd.read_csv(file1)
            new = df_1["Price"].tolist()
            df_1.drop(df_1.columns.difference(['Item','Website', 'Quantity']), 1, inplace=True)
            df_1[dt] = new
            tmp = file1.split('_', 4)[-1] 
            website=''
            for i in tmp:
                if i!='.':
                    website+=i
                else:
                    break
            
            name_of_output = 'month_'+mnth+"_"+website+'.csv'
            df_1.to_csv(name_of_output, index = False)
            
            
else:    
    files = os.listdir("E:\\Naaniz Internship\\DMART_UPDATE_ID\\Data")
    
    today_date=dnt
    transcripts_d1=[]
    transcripts_d2=[]
    for i in files:
        #print(i)
        dt_now = str(i[0])+str(i[1])
        month_now = str(i[6])+str(i[7])
        if dt_now == today_date:
            #print("Check")
            transcripts_d2.append(i)
        elif dt_now == 'mo' and month_now == mnth:
            transcripts_d1.append(i)
    
    os.chdir("E:\\Naaniz Internship\\DMART_UPDATE_ID\\Data")
    for (l, m) in itertools.zip_longest(transcripts_d1, transcripts_d2):  
        #print(l)
        #print(m)
        file1 = "E:/Naaniz Internship/DMART_UPDATE_ID/Data/"+l
        file2 = "E:/Naaniz Internship/DMART_UPDATE_ID/Data/"+m
        df_1 = pd.read_csv(file1)
        df_2 = pd.read_csv(file2)
        
        id_d1=[]
        for (i, j) in itertools.zip_longest(df_1['Item'], df_1['Quantity']): 
            id_d1.append(str(i)+str(j))
            
        id_d2=[]
        for (i, j) in itertools.zip_longest(df_2['Item'], df_2['Quantity']): 
            id_d2.append(str(i)+str(j))
            
        newcol = df_2["Price"].tolist()
        new=[]
        prev=''
        lst = id_d2
        for i in id_d1:
            flag=1
            for j in range(len(id_d2)):
                if i==lst[j] and i!=prev:
                    #print(newcol[j], end=" - ")
                    #print(lst[j])
                    prev=i
                    new.append(newcol[j])
                    flag=0
            if flag==1:
                new.append("-")
                #print("BLANK")
        
        #df_1['23-11-2020'] = df_1['Price']
        df_1[dt] = new
        
        tmp = file1.split('_', 4)[-1] 
        website=''
        for i in tmp:
            if i!='.':
                website+=i
            else:
                break
        name_of_output = 'month_'+mnth+"_"+website+'.csv'
        df_1.to_csv(name_of_output, index = False)
        
        #Delete the csv file after the data has been generated - remove the command when deployed with scraper
        os.remove(file2)
    
    
print("Program Execution Time: " + str( (time.time() - start_time)))