# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 12:02:54 2020

@author: archi
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from datetime import date


chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome('C:/Users/archi/chromedriver/chromedriver.exe', options=chrome_options)
#driver = webdriver.Chrome('C:/Users/archi/chromedriver/chromedriver.exe')


driver.get('https://www.dmart.in/')
time.sleep(0.5)

#Edit this only!!!
urls = ["https://www.dmart.in/category/school-supplies", "https://www.dmart.in/category/dmart-grocery-aesc-dmartgrocerycore", "https://www.dmart.in/category/personal-care-aesc-personalcarecore", "https://www.dmart.in/category/footwear-aesc-footwearcore", "https://www.dmart.in/category/grocery-aesc-grocerycore", "https://www.dmart.in/category/appliances-aesc-appliancescore", "https://www.dmart.in/category/dairy---beverages-aesc-dairyandbeveragescore", "https://www.dmart.in/category/home---kitchen-aesc-homeandkitchencore", "https://www.dmart.in/category/packaged-food-aesc-packagedfoodcore", "https://www.dmart.in/category/fruits---vegetables-aesc-fruitsandvegetablescore", "https://www.dmart.in/category/personal-care-aesc-personalcarecore"]
headings = ["School Suppplies", "DMart Grocery", "Personal Care", "FootWare", "Grocery", "Appliances", "Dairy & Beverages", "Home & Kitchen", "Packaged Food", "Fruits & Vegetables", "Personal Care"]

#Don't Touch!!
l=len(urls)
category=[]
names=[]
quantity=[]
price_main=[]
website=[]
city=[]
ahref_tags=[]
for i in range(l):
    time.sleep(1.5)
    count=0
    u = urls[i]
    b = headings[i]
    c = 'DMart'
    d = "Mumbai"
    #print(b)
    #Select a particular url
    driver.get(u)
    
    #Scroll to the end of the page
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
            lastCount = lenOfPage
            time.sleep(5)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
    
    
    #Start of Scraping
    item_names = driver.find_elements_by_class_name('src-client-components-product-card-vertical-card-__vertical-card-module___title')
    price = driver.find_elements_by_class_name('src-client-components-product-card-vertical-card-__vertical-card-module___amount')
    ahref_tag = driver.find_elements_by_class_name('src-client-components-product-card-vertical-card-__vertical-card-module___section-top')
    
    #Offline Start
    item_names = [item.text for item in item_names]
    for j in item_names:
        count+=1
        tmp = j.split(' : ')
        if len(tmp)<2:
            tmp.append('NaN')
        names.append(tmp[0])
        quantity.append(tmp[1])
    
    
    prices = [prices.text for prices in price]
    apn=1
    k=0
    for j in prices:
        if(k==apn):
            price_main.append(j)
            apn+=3
        k+=1
    for j in range(count):
        website.append(c)
        city.append(d)
        category.append(b)
        #print(j)
        #print(b)
    
    
    for i in ahref_tag:
        j = i.find_element_by_css_selector('a').get_attribute('href')
        res = j.split('/') 
        ahref_tags.append(res[-1])
    time.sleep(0.5) 

# terminates the application
driver.quit()

price_date = str(date.today())
col = pd.DataFrame(list(zip(website, city, category, names, quantity, ahref_tags, price_main)), columns =['Website', 'City', 'Category','Item Name','Quantity', 'ID', price_date]) 
name_of_output = price_date+'_Final_Output_DMart_ID.csv'
#col.sort_values('ID')
col.to_csv(name_of_output, index = False)

#len(pd.unique(col['ID'])) 
#len(pd.unique(col['Item Name'])) 