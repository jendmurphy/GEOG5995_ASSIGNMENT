#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jen Murphy
30 November 2017

GEOG 50995:  ASSIGNMENT

A script to reveal interesting statistics and visualise trends using publicly available datasets
released by Public Health England.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#  Set up a list of all local authorities in the Greater Manchester Health partnership
gm = ['Bolton','Bury','Manchester','Oldham','Rochdale','Salford',
          'Stockport','Tameside','Trafford','Wigan']
england = ['England']

#  Read csv file into a panda dataframe
childhealthprofiledata = pd.read_csv('Pregnancyandbirth.data.csv', encoding='cp1252')

#  Select maternal smoker status variable into a a dataframe, select lbw into a separate dataframe
smoker = childhealthprofiledata.loc[childhealthprofiledata['Indicator ID']== 20301]
lbw = childhealthprofiledata.loc[childhealthprofiledata['Indicator ID']== 92531]

#  Select only those boroughs within GM, referencing the list of GM boroughs.
gmsmoker = smoker.loc[smoker['Area Name'].isin(gm)]
gmlbw = lbw.loc[lbw['Area Name'].isin(gm)]

#  Remove unnecessary columns
gmsmoker.drop(['Area Code','Value note','Recent Trend','Lower CI 99.8 limit','Upper CI 99.8 limit','Indicator ID','Parent Code','Parent Name','Area Type','Sex','Age','Category Type', 'Category','Compared to subnational parent value or percentiles'],axis=1, inplace=True)
gmlbw.drop(['Area Code','Value note','Recent Trend','Lower CI 99.8 limit','Upper CI 99.8 limit','Indicator ID','Parent Code','Parent Name','Area Type','Sex','Age','Category Type', 'Category','Compared to subnational parent value or percentiles'],axis=1, inplace=True)

#  Two variables appended back together using df.append()
gmsmokerlbw = gmsmoker.append(gmlbw)

#  Print a list of column headers
print(gmsmoker.columns.tolist())  # eyeball check of column headers
print(gmlbw.columns.tolist())  # eyeball check of column headers

#  Stack of longitudinal data
gmsmokerpivot = gmsmoker.pivot(index = 'Area Name', columns = 'Time period')
gmlbwpivot = gmlbw.pivot(index = 'Area Name', columns = 'Time period')

#  Rename "Value" column to a unique value in the two dataframes
gmsmoker.rename(columns = {'Value':'Smokervalue'}, inplace = True)
gmlbw.rename(columns = {'Value':'LBWvalue'}, inplace = True)

#  Set index as area name for two dataframes
gmsmoker = gmsmoker.set_index('Area Name')
gmlbw = gmlbw.set_index('Area Name')

#  Join selected columns from data frames together using concat function to allow plotting.
gmsmokerlbwconcat = pd.concat([gmsmoker['Smokervalue'], gmlbw[['LBWvalue','Time period']]], axis=1)

#  Copy index to an additional column
gmsmokerlbwconcat['Area Name'] = gmsmokerlbwconcat.index

#  Plot using Seaborn package, save figure as a pdf.
scatter1 = sns.pairplot(x_vars=['Smokervalue'], y_vars=['LBWvalue'], data = gmsmokerlbwconcat, hue='Area Name', size=8)
scatter1.savefig("LBW by smoker.png") # save seaborn scatterplot

# Calculate mean and standard deviation using numpy
mean_smk = np.mean(gmsmokerlbwconcat['Smokervalue'])
st_dev_smk = np.std(gmsmokerlbwconcat['Smokervalue'])
mean_lbw = np.mean(gmsmokerlbwconcat['LBWvalue'])
st_dev_lbw = np.std(gmsmokerlbwconcat['LBWvalue'])

print(mean_smk)
print(st_dev_smk)
print(mean_lbw)
print(st_dev_lbw)

# Plotting the trend in maternal smoker rates across differnt boroughs
fig, ax = plt.subplots()
for title, group in gmsmokerlbwconcat.groupby('Area Name'):
    ax.plot(group['Time period'], group['Smokervalue'], label = title)

plt.xlabel("Year")
plt.ylabel("% of maternal smokers at delivery")
plt.title("Trend in maternal smoker rates")
plt.legend(loc=1)
fname='Trend in maternal smoker rates.pdf'
plt.savefig(fname)

#  Write manipulated data to a new Excel file for my supervisor who doesn't use Python
writer = pd.ExcelWriter('python_gm_borough_output.xlsx')
gmsmokerpivot.to_excel(writer,'gmsmokerpivot')
gmsmoker.to_excel(writer,'gmsmoker')
gmlbwpivot.to_excel(writer,'gmlbwpivot')
gmlbw.to_excel(writer,'gmlbw')
gmsmokerlbw.to_excel(writer,'gmsmokerlbw')
gmsmokerlbwconcat.to_excel(writer,'gmsmokerlbwconcat')
writer.save()


