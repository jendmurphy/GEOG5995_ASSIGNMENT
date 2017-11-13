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
data = pd.io.parsers.read_csv("Pregnancyandbirth.data.csv")

#  Select one column into a variable for testing purposes
X = data[["Indicator.ID"]]
print (X)

#  Print a list of column headers
print(data.columns.tolist())

#  Select maternal smoker status variable into a a dataframe
smoker = df.loc[data['Indicator ID']== 20301]
print(smoker)                   # eyeball check of data
print(smoker.columns.tolist())  # eyeball check of column headers

#  Set index column to local authority names (strings)
smoker = smoker.set_index(['Area Name'])

#  Select only local authorities within list(gm)
smokergm = smoker.loc[(gm)]
#smokergm.reset_index()

#  Reduce columns for ease
smokergm.drop(['Indicator Name','Indicator ID','Parent Code','Parent Name','Area Type','Sex','Age','Category Type', 'Category','Compared to subnational parent value or percentiles'],axis=1, inplace=True)
smokergm.drop(['Area Code','Recent Trend'],axis=1, inplace=True)
smokergm.drop(['Value note'],axis=1, inplace=True)

#  Eyeball check of column headers
print(smokergm)
print(smokergm.columns.tolist())

#  Rotate stacked data to give separate colums for each date
smokergmpivot = smokergm.pivot(columns= "Time period")
print(smokergmpivot)


print(smokergmpivot.columns.tolist())

smokergmpivot.plot()

plt.plot(smokergm['Value'])
plt.show()


?plt.plot

"""
melted = pd.melt(smokergm,id_vars=['Time period','Value'])
print(melted)
print(melted.columns.tolist())

smokergm = df.loc[smoker['Area Name'].isin(gm)]  #select gm LAs only into a df
print(smokergm)
print(type(smokergm))




df = pd.DataFrame({'IndicatorID':data[:,0],
                       'Area':data[:,5]})


print(df)
help(pd)







with open('Pregnancyandbirth.data.csv','rb') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, delimiter = ',')



with open('Pregnancyandbirth.data.csv') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, delimiter = ',')
    for row in reader:
            rowlist = []
            for value in row:
                rowlist.append(value)
            data.append(rowlist)
#f.close()

for row in reader:
    print (row)
    
    for row in readCSV:
        print(row[0])
with open('Pregnancyandbirth.data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')