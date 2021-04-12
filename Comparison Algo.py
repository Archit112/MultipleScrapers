# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:54:21 2020

@author: archi
"""

import os
import pandas as pd
import time

# starting time
start = time.time()

os.chdir('E:\\Naaniz Internship\\Comparison Algo')

#Load Brand Names
unrefined_brands = ['Jay Hind', 'Yash', 'Generic', 'Mama Mukhwaswala', 'Cortina', 'Purple Dew', 'Bikaji', 'Nanonine', 'Moplleez', "Haldiram's", 'Cadbury', 'Arsi', 'Vivlin', 'Gulab', 'Nutraj', 'The Kitchen Krafts', 'Kohinoor', 'Laxmipati', 'Daawat', 'Gowardhan', 'Nestle', 'Ramdev', 'Vasant', 'Rasoi Magic', 'Fortune', 'Aashirvaad', 'Sarvottam', 'Gaay Chaap', 'Uttam', 'Energetic', 'Amul', 'Aabad', 'Ankur', 'Tirupati', 'Nirma', 'Puro', 'Tata', 'Madhur', 'Dhampure', 'Rasmalai', 'NBK', 'Tata Sampann', 'Angur', 'Laxmi', 'Nutrela', 'MDH', 'SB', 'Hathi', 'Kabhi B', 'Britannia', 'Funfoods', 'Yippee', 'Rishi Rich', 'Parle', "Kellogg's", 'Dabur', 'Eastern', 'Mother', 'Kissan', 'Nutella', 'Maggi', 'Bambino', 'Knorr', 'Saffola', 'MOM', 'Lijjat', 'Talod', 
 'Weikfield', 'Swad', 'Himalaya', 'Tata Tea', 'Wagh Bakri', 'Nescafe', 'Bru', 'Complan', 'Horlicks', 'Rasna', 'Ghadi', 'Vanish', 'Wheel', 'Tide', 'Rin', 'Godrej', 'Surf Excel', 'Henko', 'Wipro', 'Ariel', 'Exo', 'Vim', 'Patanjali', 'Good Home', 'Vedee', 'Lizol', 'Colin', 'Harpic', 'Ayuhale', 'Veepee', 'Pigeon', 'Indo Fresh', 'Ambi Pur', 'All Out', 'Hit', 'Walker', 'Dentoshine', 'Head & Shoulders', 'Lakme', 'Old Spice', 'Pantene', 'Vicks', 'Whisper', 'Zandu', 'Dove', 'Santoor', 'Dettol', 'Pears', 'Lifebuoy', 'Lux', 'Sanital', 'Colgate', 'Close Up', 'Pepsodent', 'Eva', 'Fogg', 'Parachute', 'Tresemme', 'Clinic Plus', 'Nyle Naturals', 'Gillette', 'Gillette Venus', 'Wonderize', 'Veet', 'Sugar Fighter', 'Swasa', 'Moov', 'Vicco',
 'Sunsilk', 'Chik', 'BBlunt', 'Ponds', 'Freale', 'Jungle Magic', 'Signoraware', 'Varmora', 'Sizzle', 'Mastercook', 'Nayasa', 'Neo Craft', 'Crystal', 'Eureka', 'Oath Earth', 'Trueware', 'Butterfly', 'Apex', 'Nidhi', 'Rishabh', 'Nyasa', 'JVS', 'Duracell', 'Apsara', 'Nataraj', 'Aashirvaad', 'Amul', 'Babool', 'Balaji Wafers', 'Banas Dairy', 'Bakeys', 'Bisleri', 'Boroline', 'Britannia Industries', "Ching's Secret", 'Classmate', 'Dabur', 'Dalda', 'Everest Spices', 'Fevicol', 'Funskool', 'Ghari Detergent', 'Godrej', 'Gyan Dairy', 'Haathi Chaap', 'Havells', 'Lakmé Cosmetics', 'Kingfisher', 'KamaSutra', 'Linc', 'Luxor', 'MDH', 'Mankind', 'MTR Foods', 'Moods Condoms', 'Mother Dairy','Nirma', 'Nippo', 'Nippo Batteries', 'Niviva Sports',
 'Old Monk', 'Parachute', 'Parle', 'Rajesh Masala', 'Patanjali', 'Patanjali Ayurved', 'Sagar', "chhap", 'life', 'mp', 'baroda gold', 'fivestar', 'pilsbury', 'sabar', 'roller', 'pillsbury', 'traditional']

df_brands = pd.read_csv('E:/Naaniz Internship/Comparison Algo/Brand.csv')
df_brands = df_brands.loc[:,'Brand'].tolist()
for i in df_brands:
    unrefined_brands.append(i)
unrefined_brands = list(dict.fromkeys(unrefined_brands))

brands = []

#Extract cleaned brand names
checkwords = ['/', '&', '(', ')']
for i in unrefined_brands:
    for j in i.split():
        j = j.lower()
        #print(j)
        if j not in checkwords:
            brands.append(j)
brands = list(dict.fromkeys(brands))

#Load the datasets
df1 = pd.read_csv("E:/Naaniz Internship/Comparison Algo/dealshareclean.csv")
df2 = pd.read_csv("E:/Naaniz Internship/Comparison Algo/jiomartclean.csv")
df4 = pd.read_csv("C:/Users/archi/Downloads/frendycleanc.csv")


#Extract required column from imported datasets and append the data and convert to list
df1_price = df1.loc[:,'Price']
df1_site = df1.loc[:, 'Website']
df1_qty = df1.loc[:, 'Quantity']
df1_unit = df1.loc[:, 'Unit']
df1 = df1.loc[:,'Item Name']

df2_price = df2.loc[:,'Price']
df2_site = df2.loc[:, 'Website']
df2_qty = df2.loc[:, 'Quantity']
df2_unit = df2.loc[:, 'Unit']
df2 = df2.loc[:,'Item']

#Frendy Data
df4_price = df4.loc[:,'Price']
df4_site = df4.loc[:, 'Website']
df4_qty = df4.loc[:, 'Quantity']
df4_unit = df4.loc[:, 'Unit']
df4 = df4.loc[:, 'Item']

df3 = df1.append(df2)
df3 = df3.append(df4)

df3_price = df1_price.append(df2_price)
df3_price = df3_price.append(df4_price)

df3_site = df1_site.append(df2_site)
df3_site = df3_site.append(df4_site)

df3_qty = df1_qty.append(df2_qty)
df3_qty = df3_qty.append(df4_qty)

df3_units = df1_unit.append(df2_unit)
df3_units = df3_units.append(df4_unit)

#Initialize the unclean list of product names
contents = df3.tolist()
sites = df3_site.tolist()
prices = df3_price.tolist()
qty = df3_qty.tolist()
units = df3_units.tolist()

#Strip and convert to lowercase
conts=[]
check_characters = ['(', ')', "/"]
for a in contents:
    b=''
    #print("Converting "+a)
    for i in a:
        if i in check_characters:
            break
        b+=i.lower() 
    conts.append(b)
    
#print(conts)


#Exract Brand Name and Product name seperately, delete spaces and append to lists
brand_names=[]
product_names=[]
for i in conts: 
    c=''
    d=''
    for j in i.split():
        #print(j)
        if j in brands:
            c += j
            c += " "
            #print(j)
        else:
            d += j
            d += " "
    #print(c)
    brand_names.append(c)
    product_names.append(d)
    
    
#print(brand_names)
#print(product_names)

#Fuction to export data to csv
final_brands=[]
final_items=[]
final_prices=[]
final_sites=[]
final_quantity=[]    
final_units=[]
  
'''
#Saves the data to a csv file  
def savedata():
    col = pd.DataFrame(list(zip(final_brands, final_items, final_prices, final_sites, final_quantity, final_units)), columns =['Brand', 'Item', 'Price','Site','Quantity', 'Units']) 
    name_of_output = 'Output_ComparisonAlgo.csv'
    col.to_csv(name_of_output, index = False)
'''

#Function to create lists of searched for data (not sorted site prices or checked qty)
def overall(index):
    #print(brand_names[index])
    #print(product_names[index])
    #print(prices[index])
    #print(sites[index])
    #print(qty[index])
    #print("")
    final_brands.append(brand_names[index])
    final_items.append(product_names[index])
    final_prices.append(prices[index])
    final_sites.append(sites[index])
    final_quantity.append(qty[index])
    final_units.append(units[index])
    #savedata()
    #import CSV_File_Date_Cleaner

#Search for a word  
def searcher(i):
    counter = -1
    for j in product_names:
        counter+=1
        for k in j.split():
            if i in k:
                if i==k :
                    #print(j)
                    #print(counter)
                    overall(counter)

'''
name = input()
searcher(name)
'''

brand = final_brands
items = final_items
prices = final_prices
site = final_sites
qty = final_quantity  
units = final_units


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
    name_of_output = 'Final_Output_Comparison.csv'
    col.to_csv(name_of_output, index = False)
    
end = time.time()

net = (end-start)
#print('Comparison file created in ' + str(net) + ' second(s)')

