# Taken from Data Science Tutorial: https://www.youtube.com/watch?v=vmEHCJofslg
# Data from: https://github.com/KeithGalli/Pandas-Data-Science-Tasks
# Chami Lamelas
# July 2020

# Third Analysis Question:  What time should we display advertisemens to maximize the likelihood of customer’s buying product?

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("real_tasks_yt_tutorial\my_code\Sales_Data\Sales_Yearly_2019_CLEANED.csv")

# conversion to datetime object is quite intensive, even for this data set takes ~10s
# this creates a column with the hour values from the order date column, could also be
# done with string parsing (faster), but wanted to see to_datetime and dt.hour functionality
df['Purchase Hour'] = pd.to_datetime(df['Order Date']).dt.hour

# aggregate data on purchase hour and sort it on purchase hour (0-23). counting the results
# for each hour. just choosing 1 column of the counts, in this case "Quantity Ordered" 
countPerHour = df.groupby('Purchase Hour').count().sort_values('Purchase Hour')['Quantity Ordered']

# this assumes that there are no blank cells in this column, which can be checked using: 
# ref: https://stackoverflow.com/questions/29530232/how-to-check-if-any-value-is-nan-in-a-pandas-dataframe
print("checking for blank cells in Quantity Ordered: ", df['Quantity Ordered'].isnull().values().any())

print(countPerHour)

# hours in range 0-23 
hours = range(0,24)

# x-values: hours 0-23, y-values: counts per hour (sorted to be ordered 0-23)
plt.bar(hours, countPerHour)
# setting ticks to be all 24 hours 
plt.xticks(hours)
# grid is a visual benefit that allows user to more easily see y-values
plt.grid()
plt.xlabel("Hour")
plt.ylabel("Sale Count")
plt.title("Sale Count per Hour (2019)")
plt.show()





