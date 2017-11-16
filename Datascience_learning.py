#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:04:51 2017

@author: JenMurphy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly as py
import plotly.graph_objs as go
import scipy


#  Sets up dataframes
df =pd.DataFrame({'A':[2,3,1],
                  'B':[1,2,3],
                  'C':[5,3,4]})

df1 = pd.DataFrame({'A':[4],
                    'B':[4],
                    'C':[4]})

#  Adds df1 as an extra row on the bottom of df.  Columns MUST MATCH.  Adds as extra ROWS.
df = df.append(df1)

#  To reset the index column
df = df.reset_index(drop=True)

#  Setting up another dataframe
df2 = pd.DataFrame({'D':[1,2,3,4]}) 

#  Joins an additional COLUMN to the dataframe
df = pd.DataFrame.join(df,df2)

#  Making a scatterplot using a loop.  
fig, ax = plt.subplots()
for color in ['red', 'green', 'blue']:
    n = 750
    x, y = rand(2, n)
    scale = 200.0 * rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)
plt.show()

# Try to write some code that works for my data - this gives me similar to SEABORN but no colours for markers
fig, ax = plt.subplots()
for borough in gm:
    ax.scatter(gmsmokerlbwconcat['Smokervalue'],gmsmokerlbwconcat['LBWvalue'], 
               label = borough, alpha = 0.3)
ax.legend()
ax.grid(True)
plt.show()

#  Try again to plot.  It isnt pretty.
for borough in gm:
    plt.plot(gmsmokerlbwconcat['Smokervalue'],gmsmokerlbwconcat['LBWvalue'])
plt.legend(gm, loc='upper left')
plt.show()

#  Now try to sort out groups?  Would that work?  Calling the dataset df to make life easier
df = gmsmokerlbwconcat
time = ['2010','2011','2012','2013','2014','2015']

for key, grp in df.groupby(['Area Name']):
    plt.plot(df['Smokervalue'], label=key)
plt.legend(loc='best')    
plt.show()

#  This gives a set of 10 plots, seperatately
fig = plt.figure()
for title, group in df.groupby('Area Name'):
    group.plot(x='Time period', y='Smokervalue', title=title)
plt.legend()
plt.xlabel("Year")
plt.ylabel("% of maternal smokers at delivery")
plt.title("Trend in maternal smoker rates")
fname='test.pdf'
plt.savefig(fname)

?df.groupby

fig = plt.figure()
?plt.plot_date

#  Trying to get different groups plotted together.
fig = plt.figure()
for group in df.groupby('Area Name'):
    plt.plot_date(x=df['Time period'], y=df['Smokervalue'], fmt='bo-', tz=None, xdate=True,
      ydate=False, label='Area Name')

plt.legend()
plt.xlabel("Day")
plt.ylabel("Count")
plt.title("example of trying to plot more than 2 on the same figure")
fname='test.pdf'
plt.savefig(fname)

plt.plot_date(x=df.index, y=df['series2'], fmt='bo-', tz=None, xdate=True,
      ydate=False, label="d2", color='blue')

plt.plot_date(x=df.index, y=df['series3'], fmt='bo-', tz=None, xdate=True,
      ydate=False, label="d3", color='green')

plt.plot_date(x=df.index, y=df_date_domain['series4'], fmt='bo-', tz=None, xdate=True,
      ydate=False, label="d4", color='orange')

plt.plot_date(x=df.index, y=df_date_domain['series5'], fmt='bo-', tz=None, xdate=True,
      ydate=False, label="d5", color='black')

fig.autofmt_xdate()    
plt.legend()
plt.xlabel("Day")
plt.ylabel("Count")
plt.title("example of trying to plot more than 2 on the same figure")
fname='test.pdf'
plt.savefig(fname)

#Using plotly to make a table
table = py.figure_factory.create_table(df)
py.plotly.iplot(table, file_id='table of a dataframe')

# Calculate mean and standard deviation using numpy
mean_smk = np.mean(df['Smokervalue'])
st_dev_smk = np.std(df['Smokervalue'])
mean_lbw = np.mean(df['LBWvalue'])
st_dev_lbw = np.mean(df['LBWvalue'])

print(mean_smk)
print(st_dev_smk)
print(mean_lbw)
print(st_dev_lbw)


for key, grp in df.groupby(['A']):
    plt.plot(grp['B'], label=key)
    grp['D'] = pd.rolling_mean(grp['B'], window=5)    
    plt.plot(grp['D'], label='rolling ({k})'.format(k=key))
plt.legend(loc='best')    
plt.show()



?plt.line


# Define a function to create the scatterplot. This makes it easy to
# reuse code within and across notebooks
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
scatterplot(x_data = df['A']
            , y_data = df['B']
            , x_label = 'Normalized temperature (C)'
            , y_label = 'Check outs'
            , title = 'Number of Check Outs vs Temperature')




'''
# Perform linear regression
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import summary_table
x = sm.add_constant(daily_data['temp'])
y = daily_data['cnt']
regr = sm.OLS(y, x)
res = regr.fit()
# Get fitted values from model to plot
st, data, ss2 = summary_table(res, alpha=0.05)
fitted_values = data[:,2]

# Define a function for the line plot
def lineplot(x_data, y_data, x_label, y_label, title):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

# Call the function to create plot
lineplot(x_data = daily_data['temp']
         , y_data = fitted_values
         , x_label = 'Normalized temperature (C)'
         , y_label = 'Check outs'
         , title = 'Line of Best Fit for Number of Check Outs vs Temperature')