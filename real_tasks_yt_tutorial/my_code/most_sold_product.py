# Taken from Data Science Tutorial: https://www.youtube.com/watch?v=vmEHCJofslg
# Data from: https://github.com/KeithGalli/Pandas-Data-Science-Tasks
# Chami Lamelas
# July 2020

# Fifth Analysis Question: What product sold the most? Why do you think it sold the most?

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("real_tasks_yt_tutorial\my_code\Sales_Data\Sales_Yearly_2019_CLEANED.csv")

# suppose we want to see if there is a correlation between the price of a product and how many times it was sold. 
# for instance, suppose we want to say the most popular products are the cheapest and the least popular are the
# most expensive. for this reason, let's collect the rows grouped by product to perform aggregation analysis below
groupedByProduct = df.groupby('Product')

# to see the most popular products, sum on quantity ordered 
ordersPerProduct = groupedByProduct.sum()['Quantity Ordered']

# to see the average price of each product
pricePerProduct = groupedByProduct.mean()['Price Each']

print(ordersPerProduct)
print(pricePerProduct)

# storing names of products
products = list(groupedByProduct.groups.keys())

# subplots() allows the creating of multiplot figure, subplots() returns a figure and 1 axis 
fig, ax1 = plt.subplots()

# creating an "invisible" second x axis with independent y values
# https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.axes.Axes.twinx.html
ax2 = ax1.twinx()

# create a bar subplot on the first x axis (colored green) of the quantity of products ordered 
ax1.bar(products, ordersPerProduct, color = 'green')

# create a blue solid line plot using 2nd x-axis with the average price as the y-value of each product 
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html
ax2.plot(products, pricePerProduct, 'b-')

# setting labels for axis x, y-values
ax1.set_xlabel("Product")
ax1.set_ylabel("Quantity Ordered (2019)", color='g')
ax2.set_ylabel("Average Price (2019)", color='b')

# https://stackoverflow.com/questions/43152502/how-can-i-rotate-xticklabels-in-matplotlib-so-that-the-spacing-between-each-xtic
# https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.pyplot.setp.html
plt.setp(ax1.get_xticklabels(), rotation='vertical', size=8)

# sets title of figure: https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.suptitle.html
fig.suptitle('Quantity Ordered v. Average Price of Products sold 2019')
plt.show()