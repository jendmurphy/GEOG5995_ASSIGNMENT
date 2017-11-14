# -*- coding: utf-8 -*-
"""
Jen Murphy
12 October 2017

GEOG 50995:  ASSIGNMENT

A script to reveal interesting statistics using publicly available datasets
released by Public Health England.

import csv
import random
import numpy as np

"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#  Set up a list of all local authorities in the Greater Manchester Health partnership
gm = ['Bolton','Bury','Manchester','Oldham','Rochdale','Salford',
          'Stockport','Tameside','Trafford','Wigan']

#  Read csv file into a panda dataframe
childhealthprofiledata = pd.io.parsers.read_csv("/Users/JenMurphy/Documents/UNIVERSITY/PHE Data/Child health profile/Pregnancyandbirth.data.csv")

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

#  Plot using Seaborn package
sns.pairplot(x_vars=['Smokervalue'], y_vars=['LBWvalue'], data = gmsmokerlbwconcat, hue='Area Name', size=8)

#  Write manipulated data to a new Excel file
writer = pd.ExcelWriter('/Users/JenMurphy/Documents/UNIVERSITY/PHE Data/python_gm_borough_output.xlsx')
gmsmokerpivot.to_excel(writer,'gmsmokerpivot')
gmsmoker.to_excel(writer,'gmsmoker')
gmlbwpivot.to_excel(writer,'gmlbwpivot')
gmlbw.to_excel(writer,'gmlbw')
gmsmokerlbw.to_excel(writer,'gmsmokerlbw')
gmsmokerlbwconcat.to_excel(writer,'gmsmokerlbwconcat')
gm.to_excel(writer,'Local Authorities')
writer.save()



'''
#  Plot all data points as a scatter plot.  Each year of data, for each broough is represented as a distinct point.
def scatterplot(x_data, y_data, x_label, y_label, title):

    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 30, color = '#539caf', alpha = 0.75)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

# Call the function to create plot
scatterplot(x_data = gmsmoker['Value']
            , y_data = gmlbw['Value']
            , x_label = '% of Mothers reported as smokers at the time of delivery'
            , y_label = '% of all babies with a weight under 2500g'
            , title = 'Low Birthweight babies by Maternal Smoker Status, 2010-2015')


#  Join data frames together  THIS ISNT WORKING CORRECTLY YET.  NEED TO MAKE DATES MATCH
gmsmokerlbwjoin = gmsmoker.join(gmlbw, lsuffix = '_smoker', rsuffix='_lbw')

gmsmokerlbwconcat = pd.concat([df2, df1[['date', 'hour']]], axis=1)
print(df)

gmsmokerlbwjoin = gmsmokerlbwjoin.reset_index(drop=True)

?pd.DataFrame.join

gmsmokerlbwjoin = pd.DataFrame.join(gmsmoker,gmlbw)

gmsmokerlbwpivot = gmsmokerlbw.pivot(index = 'Area Name', columns = 'Indicator Name')

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
    
CODE THAT IS UNUSED OR NOT WORKING
melted = pd.melt(smokergm,id_vars=['Time period','Value'])
print(melted)
print(melted.columns.tolist())
'''