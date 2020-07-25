# Taken from Data Science Tutorial: https://www.youtube.com/watch?v=vmEHCJofslg
# Data from: https://github.com/KeithGalli/Pandas-Data-Science-Tasks
# Chami Lamelas
# July 2020

# Merge monthly data files into a single yearly CSV file

import pandas as pd 
import os 

# will hold month data of a specify year (in this case 2019)
df_yearly = pd.DataFrame()

# gets the absolute path of the directory 'Sales_Data' based off of its relative path from the current working
# directory. 
mon_data_path = os.path.abspath("real_tasks_yt_tutorial\my_code\Sales_Data")

# used following merging to make sure no rows were lost
rowCheck = 0

# loops over the files listed at the absolute path derived above 
for f in os.listdir(mon_data_path):

    # f on its own gives just the file name of a file (or dir) within the dir list
    # therefore, it must be joined with the parent absolute path (derived above) 
    f_abs_path = os.path.join(mon_data_path, f)

    # isfile() requires the input to be an absolute path 
    if os.path.isfile(f_abs_path):

        # read data from csv file utilizing absolute path
        df_mon = pd.read_csv(f_abs_path)

        # adds the number of rows in the data frame (simply the length of the index array) to rowCheck to
        # check later 
        rowCheck += len(df_mon.index)

        # merge month frame at end of year frame (ignoring original month frame index)
        df_yearly = df_yearly.append(df_mon, ignore_index=True)

# write to CSV file located in same dir as monthly data
df_yearly.to_csv(os.path.join(mon_data_path, "Sales_Yearly_2019.csv"), index=False)

# WARNING: this will include all rows of the data frames. that includes the column header row for each
# monthly file. That is, we will have the column headers appear 11 extra times in the resulting yearly
# file. 

# compare rowCheck with number of rows of merged frame
print("\nPerforming row count check: ",end="")
if (len(df_yearly.index) == rowCheck):
    print("SUCCESS")
else:
    print("FAIL. Merged row count: {merged}, Original count: {orig}".format(merged = len(df_yearly.index), orig = rowCheck))
