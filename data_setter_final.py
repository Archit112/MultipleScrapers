# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 18:15:58 2020

@author: archi
"""


import itertools
import pandas as pd  
import os

frendy = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/month_11_Frendy.csv")
grofers = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/month_11_Grofers.csv")
mehsana = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/month_11_Mehsana Mart.csv")
sanand = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/month_11_Sanand Super Mall.csv")
dealshare = pd.read_csv("E:/Naaniz Internship/DMART_UPDATE_ID/Data/month_11_Dealshare.csv")


result = pd.concat([frendy, grofers, mehsana, sanand, dealshare], axis=0)

result.to_csv('Combined Data.csv', index = False)