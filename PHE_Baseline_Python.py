#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
READING IN WARD LEVEL DATA

Created on Tue Oct 17 16:24:52 2017

@author: JenMurphy
"""

import csv
import pandas as pd
import numpy as py
import os
import matplotlib as plt
import operator

xls=pd.ExcelFile("/Users/JenMurphy/Documents/UNIVERSITY/PHE Data/Ward_2017.xlsx")
data = xls.parse('Ward',index_col=None, na_values = ['NA'])

xls=pd.ExcelFile("/Users/JenMurphy/Documents/UNIVERSITY/PHE Data/GM_Wards.xlsx")
gmwards = xls.parse('Sheet1',index_col=None, na_values = ['NA'])

gmdata = data.loc[data['AreaCode'].isin(gmwards['Ward_ID'])]
gmdata.drop(['ThemeID','Name','GeographyType'],axis=1,inplace=True)
print(gmdata.columns.tolist())

LBWgmdata = gmdata.loc[gmdata['ID']=='LH10013']  # low birth weight incidence
IMDgmdata = gmdata.loc[gmdata['ID']=='LH10010']  # IMD by ward
CHPVgmdata = gmdata.loc[gmdata['ID']=='LH10014'] # Child poverty by ward

# PLots the % of LBW by ward.  Looks a mess.
bar = LBWgmdata['Value'].plot(kind='bar')

xls=pd.ExcelFile("/Users/JenMurphy/Documents/UNIVERSITY/PHE Data/Ward_2017.xlsx")
data2 = xls.parse('Ward',index_col=None, na_values = ['NA'])







plt.hist('LBWgmdata.Value', 'LBWgmdata.AreaName', width, color="green")



y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 1/1.5

fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')










plt.figure()
df.plt(kind='hist', alpha=0.5)







print(LBWgmdata.columns.tolist())

print(gmdata)
print(LBWgmdata)
print(gmwards)



'''
gmdata = data[AreaCode isin gmwardsgroup.Ward_Id]

gmdata = pd.data.query('data.AreaCode is in gmwards.Ward_ID')


gmwardsgroup = gmwards.groupby(("Ward_ID","Local_Authority")).groups
data.pd.io.parsers.read_csv("Ward_2017)

df['s']