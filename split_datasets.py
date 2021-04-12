# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:47:02 2020

@author: archi
"""


import os
import pandas as pd

os.chdir('E:\\Naaniz Internship\\Comparison Algo')

#Load the datasets
df1 = pd.read_csv("E:/Naaniz Internship/Comparison Algo/Final_Output.csv")
df2 = pd.read_csv("E:/Naaniz Internship/Comparison Algo/Final_Output_JioMart.csv")


#Extract required column from imported datasets and append the data and convert to list
df1 = df1.loc[:,'Item Name']
df2 = df2.loc[:,'Item']
df3 = df1.append(df2)
df3 = df3.tolist()