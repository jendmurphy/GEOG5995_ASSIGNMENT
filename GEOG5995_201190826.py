#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:16:11 2017

@author: JenMurphy
"""

# -*- coding: utf-8 -*-
"""
Jen Murphy
27 October 2017

GEOG 50995:  ASSIGNMENT

A script to reveal interesting statistics using publicly available datasets
released by Public Health England.

Ella - I got SEABORN to produce a nice scatterplot, but I cant seem to work out a 
way to save this plot outside of python.

I want to plot a time series of smoker rates, with a differnet line for each borough.  
When I try to do a group_by function, I get 10 plots, rather than 10 lines on one plot.  
It is frustrating to say the least.

Any help or tips gratefully recieved!  This whole thing is driving me potty.  
I havent even tried to do anything like a regression yet.

The first chunk of code just faffs about with with the dataframe to get the bits I want.

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

#  Write manipulated data to a new Excel file
writer = pd.ExcelWriter('python_gm_borough_output.xlsx')
gmsmokerpivot.to_excel(writer,'gmsmokerpivot')
gmsmoker.to_excel(writer,'gmsmoker')
gmlbwpivot.to_excel(writer,'gmlbwpivot')
gmlbw.to_excel(writer,'gmlbw')
gmsmokerlbw.to_excel(writer,'gmsmokerlbw')
gmsmokerlbwconcat.to_excel(writer,'gmsmokerlbwconcat')
writer.save()

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

'''
#  More stuff
x = gmsmokerlbwconcat['Smokervalue']
y = gmsmokerlbwconcat['LBWvalue'], 
labels = gmsmokerlbwconcat['Area Name'] # or set in gm

for key,grp in gmsmokerlbwconcat.groupby('Area Name'):
    plt.plot(grp.Smokervalue,grp.LBWvalue,'o',label = key)
plt.legend(loc = 'best')


x = time
y = smoker rates
borough lines

#THIS IS NOT AS GOOD A GRAPH AS THE SEABORN ONE
#  Plot all data points as a scatter plot.  Each year of data, for each broough is represented as a distinct point.
def scatterplot(x_data, y_data, x_label, y_label, title):

    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 30, color = '#539caf', alpha = 0.75),

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

# Call the function to create plot
scatterplot(x_data = gmsmoker['Smokervalue']
            , y_data = gmlbw['LBWvalue']
            , x_label = '% of Mothers reported as smokers at the time of delivery'
            , y_label = '% of all babies with a weight under 2500g'
            , title = 'Low Birthweight babies by Maternal Smoker Status, 2010-2015')



#  LOOKS LIKE SEABORN BUT NO COLOUR CODING OR TITLE
# Try to write some code that works for my data - this gives me similar to SEABORN but no colours for markers
fig, ax = plt.subplots()
for borough in gm:
    ax.scatter(gmsmokerlbwconcat['Smokervalue'],gmsmokerlbwconcat['LBWvalue'], 
               label = borough, alpha = 0.3)
ax.legend()
ax.grid(True)
plt.show()

#  This gives a set of 10 plots, seperately, not all correctly named and saves just one of them - I want 10 lines on one plot!
fig = plt.figure()
group.plot(x='Time period', y='Smokervalue', title=title)
plt.legend()
plt.xlabel("Year")
plt.ylabel("% of maternal smokers at delivery")
plt.title("Trend in maternal smoker rates")
fname='test.pdf'
plt.savefig(fname)
'''