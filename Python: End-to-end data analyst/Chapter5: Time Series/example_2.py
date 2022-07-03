from ast import walk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

index = pd.date_range(start='2000-01-01', periods=200, freq='B')
ts = pd.Series(np.random.rand(len(index)), index=index)

# plt.plot(index, ts)
# plt.grid()
# plt.show()

# print(ts[1])
# print(ts['2000-01-04'])
# print(ts[datetime.datetime(2000, 1, 4)])

# print(ts['2000-01-03':'2000-01-5'])
# print()
# print(ts['2000-01-03':datetime.datetime(2000, 1, 5)])

# print(ts['2000-03':'2000-05'])

small_ts = ts['2000-02-01':'2000-02-05']
print(small_ts)
# Shift forward
print(small_ts.shift(2))
#Shift backward
print(small_ts.shift(-2))