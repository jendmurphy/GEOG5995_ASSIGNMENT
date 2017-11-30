#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:33:14 2017

Visualisation methods for GEOG5995 script

@author: JenMurphy
"""
import seaborn as sns
import matplotlib.pyplot as plt

def scatterplot(x,y,data,hue,size,title,filename):    
    #  Plot using Seaborn package, save figure as a pdf.
    sns.pairplot(x_vars=x, y_vars=y, data = data, hue=hue, size=size)
    plt.title(title)
    plt.savefig(filename)


def trendplot(data,group1,group2,group3,xlab,ylab,plottitle,fname):
    # Plotting the trend in maternal smoker rates across differnt boroughs
    fig, ax = plt.subplots()
    for title, group in data.groupby(group1):
        ax.plot(group[group2], group[group3], label = title)
    
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(plottitle)
    plt.legend(loc=1)
    plt.savefig(fname)