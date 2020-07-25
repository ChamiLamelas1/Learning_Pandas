# Taken from Data Science Tutorial: https://www.youtube.com/watch?v=vmEHCJofslg
# Data from: https://github.com/KeithGalli/Pandas-Data-Science-Tasks
# Chami Lamelas
# July 2020

# Second Analysis Question: What city sold the most product?

import pandas as pd 
import matplotlib.pyplot as plt

# parses the city (and its state) from a purchase address 
def parseCityFromAddress(addr):
    # finds the left comma (separating street, city)
    streetCitySep = addr.find(',')
    # finds the right comma (separating city, state)
    cityStateSep = addr.rfind(',')
    # city starts 2 places after street city comma and ends at city state separator 
    city = addr[streetCitySep + 2:cityStateSep]
    # state will always be 2 characters located 2 characters after city state separator 
    state = addr[cityStateSep + 2:cityStateSep + 4]
    return city + ", " + state

df = pd.read_csv("real_tasks_yt_tutorial\my_code\Sales_Data\Sales_Yearly_2019_CLEANED.csv")

# add purchase city column (includes state to avoid duplicate cities such as Portland, ME and Portland, OR)
df['Purchase City'] = df['Purchase Address'].apply(parseCityFromAddress)

# store result in temporary series 
ordersByCity = df.groupby('Purchase City').sum()['Quantity Ordered']

# printing for debugging 
print(ordersByCity)

# plotting with cities (taken from index as list) as the x values and the order counts per city as the y-values
# index is useful here as it allows x-values to match up with y-values 
plt.bar(ordersByCity.index.tolist(), ordersByCity)
# setting x-ticks to be same index list 
plt.xticks(ordersByCity.index.tolist(), rotation='vertical', size=6)
plt.xlabel("Cities")
plt.ylabel("Number of Orders")
plt.title("Cities Ranked by Number of Orders in 2019")
plt.show()


