# LEARNING PANDAS SERIES

import pandas as pd
import numpy as np

s1 = pd.Series(np.random.rand(4), 
               index=['a', 'b', 'c', 'd'])
# print(s1)
# print()

s2 = pd.Series(np.random.rand(4))
print(s2)
print()
# Reindex: if the labels do not exist in the data object, a default
# value NaN will be automatically assigned to the position
print(s2.reindex([0, 2,'b', 3]))
print()

s1['c'] = 3.14
# print(s1)

s3 = pd.Series({'001': 'Nam', '002': 'Mary', 
                '003':'Peter'})
# print(s3['002'])

s4 = pd.Series({'001': 'Nam', '002': 'Mary', 
                '003': 'Peter'}, index=[
                '002', '001', '024', '065'
                ])
# print(s4)
# print()
# print(s4.isnull())

s5 = pd.Series(2.71, index=['x', 'y'])
# print(s5)
# print()

s6 = pd.Series(np.array([2.71, 3.14]), index=['z', 'y'])
# print(s6)
# print()

# print(s5+s6)

# Use head() and tail() to show the result of first five and last n-rows of 
# the longer Series
s7 = pd.Series(np.random.rand(10000))
print(s7.head())
print()
print(s7.tail(5))