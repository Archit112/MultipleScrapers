# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:02:05 2020

@author: archi
"""

import pandas as pd
from datetime import date
import datetime
dnt = str(datetime.datetime.today().strftime('%d'))

if dnt=='1' or dnt=='01':
    df1 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/2020-11-08_Final_Output_DMart_ID.csv")
    
else:
    df1 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/11_Final_Output_DMart_ID_COMPARED.csv")

path = "E:/Naaniz Internship/DMART_UPDATE_ID/" + str(date.today()) + "_Final_Output_DMart_ID.csv"

df2 = pd.read_csv(path)

dt = str(datetime.datetime.today().strftime('%d-%m-%Y'))
mnth = str(datetime.datetime.strptime(dt, "%d-%m-%Y").month)

newcol = df2[dt].tolist()

del df2['Website']
del df2['City']
del df2['Category']
del df2['Quantity']
del df1['ID']

new=[]
prev=''
lst = df2['Item Name'].tolist()
for i in df1['Item Name']:
    flag=1
    for j in range(len(df2['Item Name'])):
        if i==lst[j] and i!=prev:
            #print(newcol[j], end=" - ")
            #print(lst[j])
            prev=i
            new.append(newcol[j])
            flag=0
    if flag==1:
        new.append("-")
        #print("BLANK")

df1[dt] = new

name_of_output = str(mnth)+'_Final_Output_DMart_ID_COMPARED.csv'

df1.to_csv(name_of_output, index = False)