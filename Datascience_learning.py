#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:04:51 2017

@author: JenMurphy
"""

import pandas as pd

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
