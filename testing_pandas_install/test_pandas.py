# https://www.learnpython.org/en/Pandas_Basics
# https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
import pandas as pd

# construct data frame object from a dictionary constructed via lists of each data type 
# list of countries, list of capitals, list of population (correspond to columns of csv file) 
inputDict = {"country":["United States of America","United Kingdom"],"capital":["Washington","London"],"population":[2000,1000]}
dictDataFrame = pd.DataFrame(inputDict)
print(dictDataFrame)
print()

# update rows to be indexed with specific labels (replace 0, 1)
dictDataFrame.index = ["US","UK"]
print(dictDataFrame)
print()

# construct data frame object from a csv file (constructed in typical manner)
# index_col parameter allows you to set the column which will be the index column (in this case, the abbreviation
# will be the index). note index column moved to th eleft
csvDataFrame = pd.read_csv("example.csv", index_col=1)
print(csvDataFrame)
print()

# single bracket indexing of a column of the data frame returns a Pandas series which is defined as:
# Series is a one-dimensional labeled array capable of holding data of any type (integer, string, 
# float, python objects, etc.). The axis labels are collectively called index (ref: Tutorialspoint)
print(csvDataFrame["country"])
print()

# the print will include a "Name" and "dtype" after the data. the name is the name of the column of the
# data frame (country in above case). the dtype is the data type (in this case an object, could be numerical
# as well). the index title (abbreviation) set on line 21 is included as well.

# double bracket indexing a column of the data frame returns a Pandas Data frame 
print(csvDataFrame[["country"]])
print()

# the print will include the country title as in the data frame printed on line 19 as well as the abbreviation
# no information is included on the data type 

# use [x:y] to print rows (called observations in Pandas) x to y-1 inclusive.
# in this case, 2nd and 3rd rows are printed (United Kingdom, France)
print(csvDataFrame[1:3])
print()

# can also use loc for index labels (of any type) and iloc for index labels (integer, i.e. default index values
# 0,1,2,...)

# this will print the 2nd row of the data frame (united kingdom) with each column element printed on an individual
# row. that is, it would print: 
# country       United Kingdom
# capital               London
# population              1000
# lastly, it prints the name of the row (from the index) associated with the row (in this case UK) and the 
# data type of the underlying data 
print(csvDataFrame.iloc[1])
print()

# by making abbreviation (csv column 1) the index column in line 20, the columns of the data are now "re-labelled"
# country (originally column 0) is still column 0, capital (originally column 2) is now column 1, population
# (originally column 3) is now column 2. this will print the population of the US (row 0).
print(csvDataFrame.iloc[0,2])
print()

# the row on the United Kingdom (with the same output as line 56) can be retrieved using loc: 
print(csvDataFrame.loc["UK"])
print()

# one can select multiple rows and multiple columns at the same time numerically (with iloc) and via labels
# (with loc)

# for instance, suppose we want to see only the country and population for rows 0 and 2, we can do: 
# note the index "changes" for the columns discussed on lines 59-61. note that the returned object from
# iloc in this case is a Pandas DataFrame
print(csvDataFrame.iloc[[0,2],[0,2]])
print()

# this same data can be retrieved using object (in this case) string labels using loc: 
print(csvDataFrame.loc[["US","FR"],["country","population"]])
print()

# one can also select multiple rows and columns via ranges both numerically (iloc) and via labels (loc)

# for instance, suppose we want to see country,capital, and population for rows 0 to 2, we can do: 
# note that the return value remains a DataFrame object (can confirm via type() call added to print())
print(csvDataFrame.iloc[0:3,0:3])
print()

# the same thing can be done using labels: 
print(csvDataFrame.loc["US":"FR","country":"population"])
print()

# OBSERVE: when using iloc, the ranges are exclusive for the upper bound. that is the to show the first 3 rows
# (indexed 0,1,2) you must supply range 0:3. The same applies for the columns. By contrast, the label ranges
# in loc are inclusive for lower and upper bounds 

# you can also select rows using loc with boolean conditions. for instance, if we wanted to restrict results 
# to rows with a population of at least 900 people (US and UK), we could do: 
print(csvDataFrame.loc[csvDataFrame["population"] >= 900])

# again, the rows can be restricted in which columns are printed. so if we wanted to say the country names of
# the rows with a population of at least 900, we do: 
print(csvDataFrame.loc[csvDataFrame["population"] >= 900,"country"])
print()

# this method will return a series of the countries of the rows that match the specified boolean condition. 
# due to this the name of the selected column (country) and type of the country (object) will appear below 
# the resulting output. 

# to have the data returned as a data frame, the second parameter (following the comma) must be a list. here are 2 
# examples (one forces the above result into data frame) and another selects multiple columns (automatically creating
# data frame). 
print(csvDataFrame.loc[csvDataFrame["population"] >= 900,["country"]])
print()

print(csvDataFrame.loc[csvDataFrame["population"] >= 900,["country","capital"]])
print()

# loc[] can also be used to update data, for instance suppose we wanted to start the country names with a population
# of at least 900. This would star the US and UK. Note that csvDataFrame["country"] on the RHS of the equals sign
# refers to the "country" column of the row with "population" >= 900 instead of the entire column as does in line 27
csvDataFrame.loc[csvDataFrame["population"] >= 900,"country"] = csvDataFrame["country"] + "*"
print(csvDataFrame)
print()



