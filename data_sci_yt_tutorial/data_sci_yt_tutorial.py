# This file contains work from going through this YouTube tutorial: https://www.youtube.com/watch?v=vmEHCJofslg
# The data used in the tutorial (and code) can be found here: https://github.com/KeithGalli/pandas
# 
# Chami Lamelas
# July 2020

import pandas as pd 

############################################# LOADING DATA #################################################

# one can read CSV, Excel (xlsx), and other separated file types (such as tab separated) into a DataFrame as 
# demonstrated below

# loading the csv file into a data frame 
df_csv = pd.read_csv("pokemon_data.csv")

# loading the excel file into a data frame
# in order to use this, the dependency 'xlrd' needed to be installed via 'pip install xlrd'
df_excel = pd.read_excel("pokemon_data.xlsx")

# loading the tab separated file (stored in txt) into data frame
# here the additional read_csv parameter 'delimiter' must be edited
# the delimiter could in theory be 'xxx' etc. 
df_tsv = pd.read_csv("pokemon_data.txt", delimiter="\t")

############################################# READING DATA #################################################

# for large files, it may be useful just to see the first (or last) few rows
# to do so, use head(n) and tail(n) for n = # rows on the desired data frame

print(df_csv.head(3))
print(df_csv.tail(3))
print(df_excel.head(3))
print(df_excel.tail(3))
print(df_tsv.head(3))
print(df_tsv.tail(3))

# from this point on, will use csv data frame

# can get column headers of data frame: 
print(df_csv.columns)

# one can iterate over the rows of the data set: 

# for index, row in df_csv.iterrows(): 
#     print(index, row)

# note that this will print a row as a series (i.e. the printing will be done as a list of the column headers
# with their associated data from the particular row). Thus, the output may not be nice to look at. 
# the following for loop allows you to select certain columns of each row and may be more useful.

# for index, row in df_csv.iterrows(): 
#     print(row[["Name","HP"]])

# note here that the index is not printed as it is printed as a Pandas Series which lists the index following
# the row data following 'Name' which is somewhat confusing given that this data set also includes a 'Name'
# column header. Therefore, for instance, the Volcanion pokemon is printed as:
# Name    Volcanion
# HP             80
# Name: 799, dtype: object <-- here 'Name' is the index 

# one can retrieve common stats on the data: 
print(df_csv.describe())
print()

############################################# SORTING DATA #################################################

# will return a sorted data frome of the data set sorted alphabetically on the 'Name' column 
# for more infor on sort_values: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
print(df_csv.sort_values('Name'))
print()

# can control the ordering using the 'ascending' parameter, such as reverse alphabetical: 
print(df_csv.sort_values('Name', ascending=False))
print()

# can also sort multiple columns. for instance, if we wanted to sort alphabetically based on 'Type 1' but with
# decreasing HP, we would do the following 
print(df_csv.sort_values(['Type 1','HP'],ascending=[1,0]))
print()

# an array of 0s and 1s is used in place of a single boolean value for ascending. A single boolean value would
# control all the columns being sorted on. This would sort BOTH 'Type 1' and 'HP' in descending order: 
print(df_csv.sort_values(['Type 1','HP'],ascending=False))
print()

############################################# EDITING DATA #################################################

# suppose that we wanted to create a column that would allow us to more easily determine the 'best' pokemon.
# this will be a 'Total' stat column that is a sum of the existing stat columns (HP, Attack, Defense, Sp. Atk,
# Sp. Def, Speed). The addition and definition of this column can be done as follows: 
df_csv['Total'] = df_csv['HP'] + df_csv['Attack'] + df_csv['Defense'] + df_csv['Sp. Atk'] + df_csv['Sp. Def'] + df_csv['Speed']
print(df_csv.head(5))
print()

# one can remove this column (or more) using 'drop()'. however, 'drop()' by default will return a data frame w/
# the removed column(s) instead of updating the invoking data frame in place (which must be specified, see the
# documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)
df_csv = df_csv.drop(columns=['Total'])
print(df_csv.head(5))
print()

# one can also remove a row (or collection of rows) using 'drop()'. 
# df_csv = df_csv.drop(index=[0])
# print(df_csv.head(5))
# print()

# one can add the 'Total' column in a quicker manner using a combination of ranges in iloc[] and sum()
# iloc[] documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html 
# sum() documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html 
# first parameter to iloc[] is : which means update should take place over all rows in the dataset 
# second parameter to iloc[] is 4:10 which means columns 4,5,6,7,8,9 (corresponding to column headers listed
# above) should be included 
# sum(axis = 1) sums the selected data over the horizontal axis (i.e. the selected columns)
df_csv['Total'] = df_csv.iloc[:,4:10].sum(axis=1)
print(df_csv.head(5))
print()

# this can be done similarly using loc (bonus of not worrying about exclusive iloc[] indexing)
# df_csv['Total'] = df_csv.loc[:,'HP':'Speed'].sum(axis=1)
# print(df_csv.head(5))
# print()

# one can rearrange the columns (more for visual sake than any effect on the data) manually by listing a new
# ordering of the columns (such as Type 1, Name, HP, etc.) with df_csv = df_csv['Type 1','Name','HP',...]
# however, for simplicity, let's say we just want to move 'Total' further left past the existing stats
# this will be done by manipulating a list of the column headers (strings) 
# ref: https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
col_headers = list(df_csv.columns.values)

# columns is an Index object, values retrieves an array of column names which is converted to a list 
df_csv = df_csv[col_headers[:4] + [col_headers[-1]] + col_headers[4:12]]
print(df_csv.head(5))
print()

############################################# SAVING DATA #################################################

# to save the contents of a data frame to a CSV file, one can use to_csv() 
# by default, the index column will be included (that is the left most column of the resulting file will be
# 0,1,2,3,...). this can be removed by the addition of index=False
df_csv.to_csv('pokemon_data_w_total.csv', index=False)

# can also save contents to an excel file, which requires module 'openpyxl' via 'pip install openpyxl'
df_csv.to_excel('pokemon_data_w_total.xlsx', index=False)

# and can convert to a tab (or other character) separated file
# here the 'sep' parameter must be used (similar to 'delimiter' in read_csv)
df_csv.to_csv('pokemon_data_w_total.txt', index=False, sep='\t')

############################################# FILTERING DATA #################################################

# one can filter data with boolean conditions using loc[], a simple condition would be: 
print(df_csv.loc[df_csv['Type 1'] == "Grass"])
print()

# compound boolean conditions are somewhat more complex. individual conditions must be surrounded in () and are
# combined using & for 'and', | for 'or'. e.g., suppose we want all pokemon with type 1 Grass and type 2 Flying
print(df_csv.loc[(df_csv['Type 1'] == "Grass") & (df_csv['Type 2'] == "Flying")])
print()

# observe that the filtered data frame (via loc[]) has the original index values (not indexed 0,1,2,...)
# in order to reset the index to 0,1,2,... (say before saving the data to a file) use reset_index() to 
# return a data frame indexed from 0 as demonstrated in the following example. the drop=True parameter is 
# necessary to stop the addition of a column with the old index values (will be titled index and is added
# by default). To see more parameters such as inplace, see reset_index doc: 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html

# here is an example with or: all pokemon with HP over 100 or Defense at least 90
print(df_csv.loc[(df_csv['HP'] > 100) | (df_csv['Defense'] >= 90)].reset_index(drop = True))
print()

# can also perform non-comparison operations inside the boolean conditions. for instance, suppose we only wanted
# to print pokemon who don't have 'Mega' in their name. Within loc[], you need to use ~ to designate 'not' and
# .str.contains to see if 'Mega' is contained in the name. For more, such as specifying case sensitivity and 
# flags (e.g. re.I is case insensitivity regex flag) 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html
# print(df_csv.loc[~df_csv['Name'].str.contains("Mega")])
# print()

######################################## CONDITIONAL CHANGES #################################################

# one can update the row data based on boolean conditions. for instance, suppose we wanted all type 1 fire 
# pokemon to be legendary. this would be done via loc[] where the first parameter is the boolean condition
# that must be satisfied to trigger a change and the second parameter is the column to be updated as a result
# df_csv.loc[df_csv['Type 1'] == "Fire", 'Legendary'] = True
# print(df_csv.head(10))
# print()

# one can update multiple columns via lists. suppose all type 1 fire pokemon are gen 10 and legendary:
# df_csv.loc[df_csv['Type 1'] == "Fire", ['Generation', 'Legendary']]=[10,True]
# print(df_csv.head(10))
# print()

######################################## AGGREGATES #########################################################

# what if you wanted to know which type 1 pokemon had the highest defense. or even more, could you order the
# type 1 classes in descending order of defense? this can be done by aggregating by type 1 class and then 
# computing the average defense of each class. this can be done as follows: 
print(df_csv.groupby('Type 1').mean().sort_values('Defense', ascending=False))
print()

# here the mean() function is used to compute the average value of each column aggregated on type 1 class.
# once this is done, the data is sorted on average defense per type 1 class in descending order. one can also
# sum the column values (using .sum()) for aggregated type 1 classes but it does not make sense in this scenario.

# in addition to .mean() and .sum() there is .count() which counts the occurrences of all non-blank rows
# per column aggregated on column. for instance, suppose we wanted to count each type 1 class. 
print(df_csv.groupby('Type 1').count())
print()

# here type 2 for instance has some empty rows, therefore the aggregated count is lower in that column than
# in other columns. to be safe (or in the case where you don't know if a column will be guaranteed to have
# all non-blank values) one can create a new column which is 1 for every row in the frame:
df_csv['count'] = 1

# now, one can count and just look at this column (returned as a series in this case)
print(df_csv.groupby('Type 1').count()['count'])
print()

# one can also aggregate based on multiple columns. that is, suppose one wanted to aggregate on the ordered
# column pair (Type 1, Type 2). that is, there would be aggregates on things like ('Bug', 'Electric') and
# remaining Type 2 classes with Type 1 'Bug' and similarly for remaining type 1 classes. 
print(df_csv.groupby(['Type 1', 'Type 2']).count()['count'])
print()

######################################## READING LARGE DATA FILES ############################################

# sometimes a data file will be too large to load into main memory all at once. instead, one can read in 
# chunks via a modification of read_csv. chunks are specified in numbers of rows. for instance, this code
# will read over a csv file 5 rows at a time:
for df in pd.read_csv('pokemon_data.csv', chunksize=5):
    print(" --- LOADING NEW CHUNK --- ")
    print(df)   

# can use this with aggregates to build a smaller (in RAM) condensed version of a large data file with selected
# info (say counts) using concat(): https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
