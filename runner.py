# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:55:00 2020

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

all_elements = df4.tolist()

elements=[]
check_characters = ['(', ')', "/"]
for a in contents:
    b=''
    #print("Converting "+a)
    for i in a:
        if i in check_characters:
            break
        b+=i.lower() 
    elements.append(b)

clean_elements=[]
for i in elements: 
    c=''
    d=''
    for j in i.split():
        #print(j)
        if j in brands:
            c += j
            c += " "
            #print(j)
        else:
            clean_elements.append(j)
    #print(c)
    
clean_elements = list(dict.fromkeys(clean_elements))

import full_comparer
for i in clean_elements:
    full_comparer.searcher(i)