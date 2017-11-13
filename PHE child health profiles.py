# -*- coding: utf-8 -*-
"""
Jen Murphy
12 October 2017

GEOG 50995:  ASSIGNMENT

A script to reveal interesting statistics using publicly available datasets
released by Public Health England.

"""
import matplotlib.pyplot as plt
import csv
import random
import numpy as np
import pandas as pd

#  Set up a list of all local authorities in the Greater Manchester Health partnership
gm = ['Bolton','Bury','Manchester','Oldham','Rochdale','Salford',
          'Stockport','Tameside','Trafford','Wigan']

#  Read csv file into a panda dataframe
childhealthprofiledata = pd.io.parsers.read_csv("/Users/JenMurphy/Documents/UNIVERSITY/PHE Data/Child health profile/Pregnancyandbirth.data.csv")

#  Select maternal smoker status variable into a a dataframe
smoker = childhealthprofiledata.loc[data['Indicator ID']== 20301]

#  Select smoker data for only those boroughs within GM, referencing the list of GM boroughs.
gmsmoker = smoker.loc[smoker['Area Name'].isin(gm)]

#  Remove unnecessary columns
gmsmoker.drop(['Indicator Name','Area Code','Value note','Recent Trend','Lower CI 99.8 limit','Upper CI 99.8 limit','Indicator ID','Parent Code','Parent Name','Area Type','Sex','Age','Category Type', 'Category','Compared to subnational parent value or percentiles'],axis=1, inplace=True)

#  Print a list of column headers
print(gmsmoker.columns.tolist())  # eyeball check of column headers

#  Stack of longitudinal data
pivot = gmsmoker.pivot(index = 'Area Name', columns = 'Time period')
print(pivot)

#  Rotate stacked data to give separate colums for each date
smokergmpivot = smokergm.pivot(columns= "Time period")
print(smokergmpivot)

#  Line plot
gmsmoker.plot.line(['Area Name','Value'])
# PLots the % of LBW by ward.  Looks a mess.
bar = gmsmoker['Value'].plot(kind='bar')

gmsmoker.plot.line([])


for borough in gm:
    tempData = gmsmoker[gmsmoker['Area Name'] == borough]
    print(tempData)
    matplotlib.pyplot.line()
matplotlib.pyplot.show()
    




"""
CODE THAT IS UNUSED OR NOT WORKING
melted = pd.melt(smokergm,id_vars=['Time period','Value'])
print(melted)
print(melted.columns.tolist())