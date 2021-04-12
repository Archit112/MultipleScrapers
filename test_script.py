# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 19:45:28 2020

@author: archi
"""
import pandas as pd
from datetime import date
import datetime
import random

df1 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/2020-11-08_Final_Output_DMart_ID.csv")

new_col=[]
for i in range(len(df1['Item Name'])):
    n = str(random.randint(0,600))
    new_col.append(str(n))
    
df2 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/2020-11-08_Final_Output_DMart_ID.csv")
del df2['08-11-2020']

dt = str(datetime.datetime.today().strftime('%d-%m-%Y'))

df2[dt] = new_col
name_of_output = dt+'_Final_Output_DMart_ID.csv'
df2.to_csv(name_of_output, index = False)

df1 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/2020-11-08_Final_Output_DMart_ID.csv")


dt = str(datetime.datetime.today().strftime('%d-%m-%Y'))
mnth = str(datetime.datetime.strptime(dt, "%d-%m-%Y").month)

newcol = df2[dt].tolist()
c2 = df2['Item Name'].tolist()

del df2['Website']
del df2['City']
del df2['Category']
del df2['Quantity']
del df1['ID']

new=[]
new2=[]
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
            new2.append(c2[j])
            flag=0
    if flag==1:
        new.append("-")
        new2.append("-")
        #print("BLANK")

df1[dt] = new
df1['Test Names (Dev)'] = new2

name_of_output = str(mnth)+'_Final_Output_DMart_ID_COMPARED.csv'

df1.to_csv(name_of_output, index = False)