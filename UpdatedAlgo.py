# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:34:06 2020

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

def stringsimilarty(frendylist, otherlist):
    threshold=80
    for otherproduct in otherlist:
        check=0
        for frendyproduct in frendylist:
            count=0
            index = otherlist.index(otherproduct)
            otherproduct=otherproduct.lower()
            frendyproduct=frendyproduct.lower()
            if check==0:
                for word in otherproduct.split():
                    for each in frendyproduct.split():
                        if word==each:
                            count=count+1
                percentage = count/len(otherproduct.split())*100
                if percentage>=threshold:
                    otherproduct=frendyproduct
                    otherlist[index] = frendyproduct
                    check=1
    return otherlist

