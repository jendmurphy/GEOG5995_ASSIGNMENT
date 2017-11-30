# GEOG5995 - Python without the hand holding!  [15 credits]

After a week of teaching with Andy Evans, we were set the task of writing some code of our very own.  The code mus - read in a file, do something with it, give some kind of output, and write that output to some kind of new file.

Simple eh?  Not so, for the python newbies.

The script here is a basic start on building the tools I'll need to manipulate large datasets coming from public health authorities in England.  The dataset used was downloaded as a .csv file from Public Health England and is a publicly available, non sensitive dataset.

Here's what it does:

1.  Reads in a .csv file, parses and put into a pandas dataframe
2.  Selects out two relevant sets of cases by question identifier number into two seperate pandas data frames
3.  Selects out relevant boroughs within each of the variable data frames  by reference to a list of borough names
4.  Drop unnecessary columns from each frame
5.  Prints a list of column headers
6.  Rename a column in each of the data frames
7.  Sets index column for each data frame, and then concatenates two data frames, and copies the index to a new column
8.  Produces a scatter plot of data and saves to a .png
9.  Calculates mean and standard deviation, and prints these values on screen
10. Appends the two variables back together as a new data frame (one variable above the other)
11. Pivots data for both dataframes to unstack longitudinal data
12. Plots time series trend for each borough as a series of subplots, using the group function, saves plot to a pdf.
13. Writes all of the manipulated data frames into a new excel file with each frame as a separate sheet so it can be sent to my supervisor who doesn't use python!
