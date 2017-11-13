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
print(gmdata.columns.tolist())


LBWgmdata = gmdata.loc[gmdata['ID']=='LH10013']
LBWgmdata.drop(['ThemeID','Name','GeographyType'], axis=1, inplace=True)

df['s']


print(LBWgmdata.columns.tolist())



print(gmdata)
print(LBWgmdata)



print(gmwards)
print



'''


gmdata = data[AreaCode isin gmwardsgroup.Ward_Id]

gmdata = pd.data.query('data.AreaCode is in gmwards.Ward_ID')


gmwardsgroup = gmwards.groupby(("Ward_ID","Local_Authority")).groups
data.pd.io.parsers.read_csv("Ward_2017)
