# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:49:20 2020

@author: archi
"""


unrefined = ['Jay Hind', 'Yash', 'Generic', 'Mama Mukhwaswala', 'Cortina', 'Purple Dew', 'Bikaji', 'Nanonine', 'Moplleez', "Haldiram's", 'Cadbury', 'Arsi', 'Vivlin', 'Gulab', 'Nutraj', 'The Kitchen Krafts', 'Kohinoor', 'Laxmipati', 'Daawat', 'Gowardhan', 'Nestle', 'Ramdev', 'Vasant', 'Rasoi Magic', 'Fortune', 'Aashirvaad', 'Sarvottam', 'Gaay Chaap', 'Uttam', 'Energetic', 'Amul', 'Aabad', 'Ankur', 'Tirupati', 'Nirma', 'Puro', 'Tata', 'Madhur', 'Dhampure', 'Rasmalai', 'NBK', 'Tata Sampann', 'Angur', 'Laxmi', 'Nutrela', 'MDH', 'SB', 'Hathi', 'Kabhi B', 'Britannia', 'Funfoods', 'Yippee', 'Rishi Rich', 'Parle', "Kellogg's", 'Dabur', 'Eastern', 'Mother', 'Kissan', 'Nutella', 'Maggi', 'Bambino', 'Knorr', 'Saffola', 'MOM', 'Lijjat', 'Talod', 
 'Weikfield', 'Swad', 'Himalaya', 'Tata Tea', 'Wagh Bakri', 'Nescafe', 'Bru', 'Complan', 'Horlicks', 'Rasna', 'Ghadi', 'Vanish', 'Wheel', 'Tide', 'Rin', 'Godrej', 'Surf Excel', 'Henko', 'Wipro', 'Ariel', 'Exo', 'Vim', 'Patanjali', 'Good Home', 'Vedee', 'Lizol', 'Colin', 'Harpic', 'Ayuhale', 'Veepee', 'Pigeon', 'Indo Fresh', 'Ambi Pur', 'All Out', 'Hit', 'Walker', 'Dentoshine', 'Head & Shoulders', 'Lakme', 'Old Spice', 'Pantene', 'Vicks', 'Whisper', 'Zandu', 'Dove', 'Santoor', 'Dettol', 'Pears', 'Lifebuoy', 'Lux', 'Sanital', 'Colgate', 'Close Up', 'Pepsodent', 'Eva', 'Fogg', 'Parachute', 'Tresemme', 'Clinic Plus', 'Nyle Naturals', 'Gillette', 'Gillette Venus', 'Wonderize', 'Veet', 'Sugar Fighter', 'Swasa', 'Moov', 'Vicco',
 'Sunsilk', 'Chik', 'BBlunt', 'Ponds', 'Freale', 'Jungle Magic', 'Signoraware', 'Varmora', 'Sizzle', 'Mastercook', 'Nayasa', 'Neo Craft', 'Crystal', 'Eureka', 'Oath Earth', 'Trueware', 'Butterfly', 'Apex', 'Nidhi', 'Rishabh', 'Nyasa', 'JVS', 'Duracell', 'Apsara', 'Nataraj', 'Aashirvaad', 'Amul', 'Babool', 'Balaji Wafers', 'Banas Dairy', 'Bakeys', 'Bisleri', 'Boroline', 'Britannia Industries', "Ching's Secret", 'Classmate', 'Dabur', 'Dalda', 'Everest Spices', 'Fevicol', 'Funskool', 'Ghari Detergent', 'Godrej', 'Gyan Dairy', 'Haathi Chaap', 'Havells', 'Lakmé Cosmetics', 'Kingfisher', 'KamaSutra', 'Linc', 'Luxor', 'MDH', 'Mankind', 'MTR Foods', 'Moods Condoms', 'Mother Dairy','Nirma', 'Nippo', 'Nippo Batteries', 'Niviva Sports',
 'Old Monk', 'Parachute', 'Parle', 'Rajesh Masala', 'Patanjali', 'Patanjali Ayurved']
refined = []

checkwords = ['/', '&', '(', ')']
for i in unrefined:
    for j in i.split():
        j = j.lower()
        #print(j)
        if j not in checkwords:
            refined.append(j)
        
refined = list(dict.fromkeys(refined))