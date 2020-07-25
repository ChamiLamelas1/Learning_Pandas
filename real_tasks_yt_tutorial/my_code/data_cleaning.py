# Taken from Data Science Tutorial: https://www.youtube.com/watch?v=vmEHCJofslg
# Data from: https://github.com/KeithGalli/Pandas-Data-Science-Tasks
# Chami Lamelas
# July 2020

# Data Cleaning before analysis question

import pandas as pd

df = pd.read_csv("real_tasks_yt_tutorial\my_code\Sales_Data\Sales_Yearly_2019.csv")

#################################### CLEANING THE DATA #################################################

# this will return a new Data frame that removes rows with all NaN values.
# the axis parameter is default 0 (i.e. rows or index), but to remove all NaN columns set axis = 1
# how determines whether all or any of the columns in a row must be NaN to be removed (default is any)
# doc: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
df = df.dropna(how='all')

# number of rows pre filtering of duplicated column headers from merging 
rowsPreFilter = len(df.index)

print(df.loc[df['Order Date'] == "Order Date"])

# as indicated in merge_monthly.py documentation (used to create data file), the column headers would be
# duplicated. therefore, these rows must also be removed. this can be done via filtering (that is updating
# df to be all rows that do not contain the string "Order Date" for instance in the 'Order Date' column)
# it also can be done via dropping rows from an index, but that seems to be slower
# ref: https://stackoverflow.com/questions/13851535/delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression-involving
df = df.loc[~(df['Order Date'] == "Order Date")].reset_index(drop = True)

print("\nROWS REMOVED = {0}".format(rowsPreFilter - len(df.index)))

# before we can create the 'Total Sales Price' column discussed later, the 'Quantity Ordered' and 'Price Each'
# columns don't seem be to working properly in the multiplication. can see the data types of these columns: 
print("\nDATA FRAME SCHEMA:\n", df.dtypes)

# we can see that 'Quantity Ordered' and 'Price Each' are both not numeric, can use pandas to_numeric utility
# instead of as_type(). it allows automatic size fitting in addition to other features:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
df['Price Each'] = pd.to_numeric(df['Price Each'])

# can see updated schema here (quantity ordered -> int, price each -> float)
print("\nUPDATED FRAME SCHEMA:\n", df.dtypes)

# writing cleaned data to new CSV: 
df.to_csv("real_tasks_yt_tutorial\my_code\Sales_Data\Sales_Yearly_2019_CLEANED.csv", index=False)

