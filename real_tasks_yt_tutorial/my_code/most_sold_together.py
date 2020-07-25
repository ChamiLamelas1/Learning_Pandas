# Taken from Data Science Tutorial: https://www.youtube.com/watch?v=vmEHCJofslg
# Data from: https://github.com/KeithGalli/Pandas-Data-Science-Tasks
# Chami Lamelas
# July 2020

# Fourth Analysis Question:  products are most often sold together?

import pandas as pd 
# https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter
# https://www.geeksforgeeks.org/permutation-and-combination-in-python/
from itertools import combinations

df = pd.read_csv("real_tasks_yt_tutorial\my_code\Sales_Data\Sales_Yearly_2019_CLEANED.csv")

# create a new column in the frame that for a given sale will hold all the products that are in the order for which
# the sale is contained in. This will be done by aggregating rows on the order ID. Then, the grouped Products in the 
# order will be concatenated into a list. transform() will operate on a lambda function that maintains the same number
# of rows that can then be loaded into the 'Order Products' column.
df['Order Products'] = df.groupby('Order ID')['Product'].transform(lambda x : ','.join(x))

# note that sales in the same order (id) will have the same 'Order Products' as well. The columns of interest are the 
# unique 'Order ID' and 'Order Products' columns which can be filtered using drop_duplicates() of just those 2 columns.
df = df[['Order ID', 'Order Products']].drop_duplicates()

c = Counter() 

# iterating over the rows of the data frame
for index,row in df.iterrows():
    # get a list of the order products by splitting up the string. while this seems less efficient to conver to a string 
    # and then break it up, it means that strings will be stored in duplicates and are removed. only lists are created for 
    # unique orders 
    orderProducts = row['Order Products'].split(',')

    # get all the pairs of products in the order using combinations (binomial coeff)
    productPairs = combinations(orderProducts, 2)

    # Counter.update() will update all the pairs in the input list to have 1 more occurrence in the Counter
    c.update(productPairs)

# for each tuple (pair, count of pair in sales), print it 
for pairCount in c.most_common(10):
    print(pairCount)



