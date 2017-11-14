#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LocalHealth.org WARD LEVEL DATA

Created on Tue Oct 17 16:24:52 2017

@author: JenMurphy
"""

import csv
import pandas as pd
import numpy as py
import os
import matplotlib as plt
import operator

#  Read in excel file from localhealth.org
xls=pd.ExcelFile("/Users/JenMurphy/Documents/UNIVERSITY/PHE Data/Ward_2017.xlsx")
data = xls.parse('Ward',index_col=None, na_values = ['NA'])

#  Read in excel file containing list of wards within GM
xls=pd.ExcelFile("/Users/JenMurphy/Documents/UNIVERSITY/PHE Data/GM_Wards.xlsx")
gmwards = xls.parse('Sheet1',index_col=None, na_values = ['NA'])

#  Select out GM ward data from whole dataset 
gmdata = data.loc[data['AreaCode'].isin(gmwards['Ward_ID'])]
gmdata.drop(['ThemeID','Name','GeographyType'],axis=1,inplace=True)
print(gmdata.columns.tolist())

LBWgmdata = gmdata.loc[gmdata['ID']=='LH10013']  # low birth weight incidence
IMDgmdata = gmdata.loc[gmdata['ID']=='LH10010']  # IMD by ward
CHPVgmdata = gmdata.loc[gmdata['ID']=='LH10014'] # Child poverty by ward

#  Write manipulated data to a new Excel file
writer = pd.ExcelWriter('/Users/JenMurphy/Documents/UNIVERSITY/PHE Data/python_ward_output.xlsx')
LBWgmdata.to_excel(writer,'LBW')
IMDgmdata.to_excel(writer,'IMD')
CHPVgmdata.to_excel(writer,'Child Poverty')
writer.save()


# PLots the % of LBW by ward.  Looks a mess.
bar = LBWgmdata['Value'].plot(kind='bar')








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