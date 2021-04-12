# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:39:27 2020

@author: archi
"""

import pandas as pd
import numpy as np
import re
import os
import warnings
warnings.filterwarnings('ignore')
from bs4 import BeautifulSoup
import json
import io
import requests
from selenium import webdriver
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

State = 'Gujarat'
loc_dict={'Andhra Pradesh':'530001','Arunachal Pradesh':'791111','Assam':'781001','Bihar':'800001',
     'Chandigarh':'160036','Chhattisgarh':'495001','Dadra and Nagar Haveli and Daman and Diu':'400001',
      'Delhi':'110001','Goa':'403001','Gujarat':'380001','Haryana':'121001','Himachal Pradesh':'171001','Jammu and Kashmir':'190001',
     'Jharkhand':'834001','Karnataka':'560002','Kerala':'682001','Ladakh':'194101','Lakshadweep':'682001','Madhya Pradesh':'482001',
     'Maharashtra':'400001','Manipur':'795001','Meghalaya':'793001','Mizoram':'78100','Nagaland':'78100','Odisha':'751001','Puducherry':'600001',
     'Punjab':'140001','Rajasthan':'302001','Sikkim':'737101','Tamil Nadu':'600001','Telangana':'500001','Tripura':'799001',
     'Uttar Pradesh':'22602','Uttarakhand':'248001','West Bengal':'700001'}

df = pd.DataFrame(columns=['Website','City','Category','Item','Quantity','Price'])
links=['https://www.jiomart.com/category/groceries/fruits-vegetables/page/','https://www.jiomart.com/category/groceries/dairy-bakery/page/','https://www.jiomart.com/category/groceries/staples/page/','https://www.jiomart.com/category/groceries/snacks-branded-foods/page/','https://www.jiomart.com/category/groceries/fruits-vegetables/fresh-fruits/page/','https://www.jiomart.com/category/groceries/fruits-vegetables/fresh-vegetables/page/','https://www.jiomart.com/category/groceries/fruits-vegetables/herbs-seasonings/page/','https://www.jiomart.com/category/groceries/fruits-vegetables/exotic-fruits-vegetables/page/',
   'https://www.jiomart.com/category/groceries/dairy-bakery/dairy/page/','https://www.jiomart.com/category/groceries/dairy-bakery/toast-khari/page/','https://www.jiomart.com/category/groceries/dairy-bakery/cakes-muffins/page/','https://www.jiomart.com/category/groceries/dairy-bakery/breads-and-buns/page/','https://www.jiomart.com/category/groceries/dairy-bakery/bakery-snacks/page/','https://www.jiomart.com/c/groceries/staples/atta-flours-sooji/26/page/','https://www.jiomart.com/c/groceries/staples/dals-pulses/17/page/','https://www.jiomart.com/c/groceries/staples/rice-rice-products/14/page/','https://www.jiomart.com/c/groceries/staples/edible-oils/58/page/','https://www.jiomart.com/c/groceries/staples/dry-fruits/31/page/','https://www.jiomart.com/c/groceries/staples/masalas-spices/21/page/','https://www.jiomart.com/c/groceries/staples/salt-sugar-jaggery/23/page/','https://www.jiomart.com/c/groceries/staples/soya-products-wheat-other-grains/106/page/', 
   'https://www.jiomart.com/category/groceries/snacks-branded-foods/biscuits-cookies/page/','https://www.jiomart.com/category/groceries/snacks-branded-foods/noodle-pasta-vermicelli/page/','https://www.jiomart.com/category/groceries/snacks-branded-foods/breakfast-cereals/page/','https://www.jiomart.com/category/groceries/snacks-branded-foods/snacks-namkeen/page/','https://www.jiomart.com/category/groceries/snacks-branded-foods/chocolates-candies/page/','https://www.jiomart.com/category/groceries/snacks-branded-foods/ready-to-cook-eat/page/','https://www.jiomart.com/category/groceries/snacks-branded-foods/spreads-sauces-ketchup/page/','https://www.jiomart.com/category/groceries/snacks-branded-foods/indian-sweets/page/','https://www.jiomart.com/category/groceries/snacks-branded-foods/pickles-chutney/page/']
for link in links:
    df_2=pd.DataFrame(columns=['Website','City','Category','Item','Quantity','Price'])
    for Page in range(1,5):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(executable_path='C:/Users/archi/chromedriver/chromedriver.exe',chrome_options =chrome_options)
            driver.get(link+'{0}'.format(Page))
            driver.find_element_by_class_name('delivery_content').click()
            driver.find_element_by_class_name('inp_text').send_keys(loc_dict[State])
            driver.find_element_by_class_name('apply_btn').click()
            time.sleep(1)
            resp = driver.execute_script('return document.documentElement.outerHTML')
            soup = BeautifulSoup(resp,'lxml')
            k=soup.find_all('div',class_='col-md-3 p-0')
            I = list(map(lambda x: x.find_all('span',class_='clsgetname'),k))
            P = list(map(lambda x: x.find_all('span',{'id':'final_price'}),k))
            df_1 = pd.DataFrame(columns=['Website','City','Category','Item','Quantity','Price'])
            df_1['Item']=list(map(lambda x: x[0].text,I))
            df_1['Price'] = list(map(lambda x: float(re.sub(string=x[0].text,pattern='₹',repl='')),P))
            df_2 = df_2.append(df_1,ignore_index=True) 
            df_2['Category'] =link.split('/')[6].capitalize().replace('-',' ')
            df = df.append(df_2,ignore_index=True)
        except Exception as ex:
            break        
    
    
    #df['Quantity'] = df['Quantity'].apply(lambda x: str(x).replace('[','').replace(']','').replace("'",''))
    
    
df['City']= 'Ahmedabad'
df['Website']='JioMart'
df = df[['Website','City','Category','Item','Quantity','Price']]
df['Quantity'] = df.Item.apply(lambda x:  str(re.findall('[0-9]{1,3}[' '] [a-zA-Z]{1,3}',x)).replace('[','').replace(']','').replace("'",'').replace(' ',''))
df['Item'] = df['Item'].apply(lambda x: re.sub('[0-9]{1,3}[' '] [a-zA-Z]{1,3}','',x))
df.drop_duplicates(inplace=True)
df = df.reset_index().drop('index',axis=1)
#driver.quit

name_of_output = 'Final_Output_JioMart.csv'
df.to_csv(name_of_output, index = False)