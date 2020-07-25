# Taken from Data Science Tutorial: https://www.youtube.com/watch?v=vmEHCJofslg
# Data from: https://github.com/KeithGalli/Pandas-Data-Science-Tasks
# Chami Lamelas
# July 2020

# First Analysis Question: What was the best month for sales? How much was earned that month?

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("real_tasks_yt_tutorial\my_code\Sales_Data\Sales_Yearly_2019_CLEANED.csv")

#################################### ADD NUMERICAL MONTH COL #################################################

# sets month column first 2 characters of order date (string type)
df['Order Month'] = df['Order Date'].str[0:2]

# can cast a column using astype(), here to int32. this will yield an error if some values cannot be converted
# to int32 (for instance if there are non integer strings or floating point values such as NaN)
# doc: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html
df['Order Month'] = df['Order Month'].astype('int32')

print(df.head())

################################### BEST MONTH FOR SALES? ##################################################

# Observe that the price of a given sale is dependent on 2 columns: Quantity Ordered and the Price of each item.
# More specifically, we want to aggregate the months and then sum over the month (quantity ordered x price)
# To do tihs, let's create a column "Total Sale" which is this value 
df['Total Sale'] = df['Quantity Ordered'] * df['Price Each']
print(df.head())

# now that this column has been added, lets perform the aggregation sum analysis. That is, aggregate the 
# month 'Total Sale' data and then sum it. The printed data will show the sales in decreasing order.
print(df.groupby('Order Month').sum().sort_values('Total Sale', ascending=False)['Total Sale'])

#################################### PLOTTING THE RESULTS #################################################

# x-axis: months ordered 1-12 
monthValues = range(1,13)
# y-axis: aggregated data now sorted on order month, just 'Total Sales'
monthlyTotals = df.groupby('Order Month').sum().sort_values('Order Month')['Total Sale']

# bar graph, setting x, y data: 
plt.bar(monthValues, monthlyTotals)
# makes ticks on x-axis 1-12 
plt.xticks(monthValues)
# labels for x,y axis
plt.xlabel("Months")
plt.ylabel("Total Sale")
plt.title("Total Sale for Each Month in 2019")
plt.show()






    

