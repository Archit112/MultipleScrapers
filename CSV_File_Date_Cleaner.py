# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:34:57 2020

@author: archi
"""


import os
import pandas as pd

os.chdir('E:\\Naaniz Internship\\Comparison Algo')

df = pd.read_csv("E:/Naaniz Internship/Comparison Algo/Output_ComparisonAlgo.csv")
df = df.sort_values(by=['Item', 'Price', 'Quantity'])

items = df.loc[:,'Item'].tolist()
prices = df.loc[:,'Price'].tolist()
brand = df.loc[:,'Brand'].tolist()
qty = df.loc[:,'Quantity'].tolist()
site = df.loc[:,'Site'].tolist()
units = df.loc[:, 'Units']


ds_price=[]
ds_brand=[]
ds_item=[]
ds_qty=[]
ds_unit=[]

jiomart_price=[]
jiomart_brand=[]
jiomart_item=[]
jiomart_qty=[]
jiomart_unit=[]

frendy_price=[]
frendy_brand=[]
frendy_item=[]
frendy_qty=[]
frendy_unit=[]

counter=-1
for i in site:
    counter+=1
    if i == 'DS':
        ds_price.append(prices[counter])
        ds_brand.append(brand[counter])
        ds_item.append(items[counter])
        ds_qty.append(qty[counter])
        ds_unit.append(units[counter])
    elif i == 'JioMart':
        jiomart_price.append(prices[counter])
        jiomart_brand.append(brand[counter])
        jiomart_item.append(items[counter])
        jiomart_qty.append(qty[counter])
        jiomart_unit.append(units[counter])
    elif i == 'Frendy':
        frendy_price.append(prices[counter])
        frendy_brand.append(brand[counter])
        frendy_item.append(items[counter])
        frendy_qty.append(qty[counter])
        frendy_unit.append(units[counter])
    #print(counter)


final_brands = []
final_items = []
final_qty = []
final_unit = []
final_price_frendy = []
final_price_ds = []
final_price_jiomart = []
prev_item=''

for i in frendy_item:
    
    if i in ds_item:
        
        index = ds_item.index(i)
        index_frendy = frendy_item.index(i)
        
        if frendy_brand[index_frendy] == ds_brand[index]  and i != prev_item and frendy_qty[index_frendy] == ds_qty[index]:         
            print('Found in DS: ' + i + 'at ' + str(index))
            final_brands.append(frendy_brand[index_frendy])
            final_items.append(i)
            final_price_frendy.append(frendy_price[index_frendy])
            final_price_ds.append(ds_price[index])
            final_price_jiomart.append('-')
            final_qty.append(frendy_qty[index_frendy])
            final_unit.append(frendy_unit[index_frendy])
            prev_item = i
            
        
    elif i in jiomart_item:
        
        index = jiomart_item.index(i)
        index_frendy = frendy_item.index(i)
        
        if frendy_brand[index_frendy] == jiomart_brand[index] and i != prev_item and frendy_qty[index_frendy] == jiomart_qty[index]:         
            print('Found in Jiomart: ' + i + 'at ' + str(index))
            final_brands.append(frendy_brand[index_frendy])
            final_items.append(i)
            final_price_frendy.append(frendy_price[index_frendy])
            final_price_ds.append('-')
            final_price_jiomart.append(jiomart_price[index])
            final_qty.append(frendy_qty[index_frendy])
            final_unit.append(frendy_unit[index_frendy])
            prev_item = i
   

if len(final_items) == 0:
    print('No match found')
else:
    print(final_items)
    print(final_price_frendy)
    print(final_price_ds)
    print(final_price_jiomart)
    print(final_brands)
    print(final_qty)
    print(final_unit)
    col = pd.DataFrame(list(zip(final_brands, final_items, final_qty, final_unit, final_price_frendy, final_price_ds, final_price_jiomart)), columns =['Brand Name', 'Item Name', 'Quantity', 'Unit', 'Frendy Price', 'DealShare Price', 'JioMart Price']) 
    name_of_output = 'Final_Output_ComparisonAlgo.csv'
    col.to_csv(name_of_output, index = False)