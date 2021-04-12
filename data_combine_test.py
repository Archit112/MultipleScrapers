# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:12:16 2020

@author: archi
"""


import itertools
import pandas as pd  
from datetime import date
import datetime

dnt = str(datetime.datetime.today().strftime('%d'))


#Sanand
df_sanand_1 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/23-11-2020_Sanand Super Mall.csv")
df_sanand_2 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/24-11-2020_Sanand Super Mall.csv")

id_d1=[]
for (i, j) in itertools.zip_longest(df_sanand_1['Item'], df_sanand_1['Quantity']): 
    id_d1.append(str(i)+str(j))
    
id_d2=[]
for (i, j) in itertools.zip_longest(df_sanand_2['Item'], df_sanand_2['Quantity']): 
    id_d2.append(str(i)+str(j))
    
newcol = df_sanand_2["Price"].tolist()
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

df_sanand_1['Day 1'] = df_sanand_1['Price']
df_sanand_1['Day 2'] = new



#Mehsana
df_mehsana_1 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/23-11-2020_Mehsana Mart.csv")
df_mehsana_2 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/24-11-2020_Mehsana Mart.csv")

id_d1=[]
for (i, j) in itertools.zip_longest(df_mehsana_1['Item'], df_mehsana_1['Quantity']): 
    id_d1.append(str(i)+str(j))
    
id_d2=[]
for (i, j) in itertools.zip_longest(df_mehsana_2['Item'], df_mehsana_2['Quantity']): 
    id_d2.append(str(i)+str(j))
    
newcol = df_mehsana_2["Price"].tolist()
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

df_mehsana_1['Day 1'] = df_mehsana_1['Price']
df_mehsana_1['Day 2'] = new


#DealShare
df_dealshare_1 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/23-11-2020_Dealshare.csv")
df_dealshare_2 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/24-11-2020_Dealshare.csv")

id_d1=[]
for (i, j) in itertools.zip_longest(df_dealshare_1['Item Name'], df_dealshare_1['Quantity']): 
    id_d1.append(str(i)+str(j))
    
id_d2=[]
for (i, j) in itertools.zip_longest(df_dealshare_2['Item Name'], df_dealshare_2['Quantity']): 
    id_d2.append(str(i)+str(j))
    
newcol = df_dealshare_2["Price"].tolist()
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

df_dealshare_1['Day 1'] = df_dealshare_1['Price']
df_dealshare_1['Day 2'] = new


#DMart
df_dmart_1 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/23-11-2020_Dmart.csv")
df_dmart_2 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/24-11-2020_Dmart.csv")

id_d1=[]
for (i, j) in itertools.zip_longest(df_dmart_1['Item Name'], df_dmart_1['Quantity']): 
    id_d1.append(str(i)+str(j))
    
id_d2=[]
for (i, j) in itertools.zip_longest(df_dmart_2['Item Name'], df_dmart_2['Quantity']): 
    id_d2.append(str(i)+str(j))
    
newcol = df_dmart_2["Price"].tolist()
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

df_dmart_1['Day 1'] = df_dmart_1['Price']
df_dmart_1['Day 2'] = new


#Frendy
df_frendy_1 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/23-11-2020_Frendy.csv")
df_frendy_2 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/24-11-2020_Frendy.csv")

id_d1=df_frendy_1['Item_url']    
id_d2=df_frendy_2['Item_url']
    
newcol = df_frendy_2["Price"].tolist()
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

df_frendy_1['Day 1'] = df_frendy_1['Price']
df_frendy_1['Day 2'] = new

#Grofers
df_grofers_1 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/23-11-2020_Grofers.csv")
df_grofers_2 = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/24-11-2020_Grofers.csv")

id_d1=[]
for (i, j) in itertools.zip_longest(df_grofers_1['Item'], df_grofers_1['Quantity']): 
    id_d1.append(str(i)+str(j))
    
id_d2=[]
for (i, j) in itertools.zip_longest(df_grofers_2['Item'], df_grofers_2['Quantity']): 
    id_d2.append(str(i)+str(j))
    
newcol = df_grofers_2["Price"].tolist()
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

df_grofers_1['Day 1'] = df_grofers_1['Price']
df_grofers_1['Day 2'] = new


#Output Statements
name_of_output = 'Final_Output_DMart_ID_COMPARED.csv'
df_dmart_1.to_csv(name_of_output, index = False)

name_of_output = 'Final_Output_Dealshare_ID_COMPARED.csv'
df_dealshare_1.to_csv(name_of_output, index = False)

name_of_output = 'Final_Output_Frendy_ID_COMPARED.csv'
df_frendy_1.to_csv(name_of_output, index = False)

name_of_output = 'Final_Output_Sanand_ID_COMPARED.csv'
df_sanand_1.to_csv(name_of_output, index = False)

name_of_output = 'Final_Output_Mehsana_ID_COMPARED.csv'
df_mehsana_1.to_csv(name_of_output, index = False)

name_of_output = 'Final_Output_Grofers_ID_COMPARED.csv'
df_grofers_1.to_csv(name_of_output, index = False)