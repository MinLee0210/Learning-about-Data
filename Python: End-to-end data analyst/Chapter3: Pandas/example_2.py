# LEARNING PANDAS DATAFRAME
# The Dataframe is a tabular data structure (is a table in short) comprising
# a set of ordered columns and rows (it can be thought as a group of Series object
#                                     that share an index)

from textwrap import fill
import pandas as pd
import numpy as np

data = {'Year': [2000, 2005, 2010, 2014], 
        'Median_Age': [24.2, 26.4, 28.5, 30.3], 
        'Density': [244, 256, 268, 279]}
df1 = pd.DataFrame(data)
# print(df1)

# Reindex: if the labels do not exist in the data object, a default
# value NaN will be automatically assigned to the position
# print(df1.reindex(index=[0, 2, 'b, 3'], 
#                   columns=['Density', 'Year', 'Median_Age', 'C']))
# print()

df2 = pd.DataFrame(data, columns=['Year', 'Density', 'Median_Age'])
# print(df2)
# print(df2.index)

df3 = pd.DataFrame(data, 
                   columns=['Year', 'Density', 'Median_Age'], 
                   index=['a', 'b', 'c', 'd'])
# print(df3)
# print(df3.index)

df4 = pd.DataFrame([
    ['Peter', 16, 'pupil', 'TN', 'M', None], 
    ['Mary', 21, 'student', 'SG', 'F', None],
    ['Nam', 22, 'student', 'HN', 'M', None],
    ['Mai', 31, 'nurse', 'SG', 'F', None],
    ['John', 28, 'laywer', 'SG', 'M', None]],
    columns=['Name', 'Age', 'Career', 'Province', 'Sex', 'Award'])
# print(df4)
# print()
# print(df4.Name)
# print()

# Appending a new column named New
# df4['New'] = None 
# print(df4)
# print()

# Dropping the column by using df.drop(), 
# first place is the chosen column, the axis equal to 0 is row, 1 is column,
# inplace = True means that  specifies the drop operation should happen in same dataframe and 
# no copy of the dataframe should be created
# df4.drop(df4.columns[-1], axis=1, inplace=True)
# print(df4)
# print()

# Retrieving row by position or name
# print(df4.iloc[2])
# print()

# Binary operations
df5 = pd.DataFrame(np.arange(9).reshape(3, 3),
                   columns=['a', 'b', 'c'])
# print(df5)
# print()

df6 = pd.DataFrame(np.arange(8).reshape(2, 4), 
                   columns=['a', 'b', 'c', 'd'])
# print(df6)
# print()

# and-operation is like and in logic, if there is no identical between
# dataframes, the NaN values will be automatically assigned to the field, 
# else, it will add up the value
# print(df5 + df6)
# print()

# In case we want to fill with a fixed value, we use some built-in functions
# such as add, sub, div and mul that support fill_value
# print(df5.add(df6, fill_value=0))
# print()
# print(df5.sub(df6, fill_value=0))
# print()
# print(df5.mul(df6, fill_value=1))
# print()
# print(df5.div(df6, fill_value=1))

# Statistical functions
# print(df5.describe())
# print()
# print(df5.describe(percentiles=[0.5, 0.8]))
# print(df5.apply(np.std, axis=1))

# Using function 
# Using lambda function
# Take each column then use its max subtracts its min
f = lambda x: x.max() - x.min()
# print(df5.apply(f, axis = 1))
# Using define function
def sigmoid(x):
    return 1/(1 + np.exp(x))
# print(df5.apply(sigmoid))

# Sorting
df7 = pd.DataFrame(np.arange(12).reshape(3, 4), 
                   columns=['b', 'd', 'a', 'c'], 
                   index=['x', 'a', 'z'])
# print(df7)
# print()
# # Sort by index
# print(df7.sort_index(axis=1))
# print()
# print(df7.sort_index(axis=0))
# print()

df8 = pd.DataFrame(np.random.rand(12).reshape(4, 3), 
                   columns=['a', 'b', 'c'])

# print(df8)
# print()
# print(df8.cov())
# print()
# print(df8.corr(method='spearman'))
# print()
# print(df8.corr(method='kendall'))
# print()
# print(df8.corr(method='pearson'))
# print()

# df9 = pd.DataFrame(np.arange(8).reshape(4, 2), 
#                    columns=['a', 'b'])
# print(df9)
# print()
# print(df8.corrwith(df9))

df = pd.DataFrame(np.random.rand(12).reshape(4, 3), 
                  index=[['a', 'a', 'b', 'b'], 
                        [0, 1, 0, 1]], 
                  columns=[['x', 'x', 'y'], [0, 1, 0]])
print(df)
print()
print(df.index)
print()
print(df.columns)
print()
print(df['x'])
