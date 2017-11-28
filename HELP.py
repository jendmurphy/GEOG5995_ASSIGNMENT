#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:05:09 2017

@author: JenMurphy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sin = np.sin
cos = np.cos
pi = np.pi
N = 100

x = np.linspace(0, pi, N)
a = sin(x)
b = cos(x)

df = pd.DataFrame({
    'A': [True]*N + [False]*N,
    'B': np.hstack((a,b))
    })

for key, grp in df.groupby(['A']):
    plt.plot(grp['B'], label=key)
    grp['D'] = pd.rolling_mean(grp['B'], window=5)    
    plt.plot(grp['D'], label='rolling ({k})'.format(k=key))
plt.legend(loc='best')    
plt.show()


df=gmsmokerlbwconcat
for key, grp in df.groupby(['Area Name']):
    plt.plot(grp['Smokervalue'], label=key)
plt.legend(loc='best')    
plt.show()