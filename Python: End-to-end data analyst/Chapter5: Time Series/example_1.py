# WORKING WITH DATE AND TIME OBJECTS
import datetime
import pandas as pd
import numpy as np

# print(datetime.datetime(2000, 1, 1))
# print(datetime.datetime.strptime("2000/1/1", "%Y/%m/%d"))
# print(datetime.datetime(2000, 1, 1, 0, 0).strftime("%Y%m%d"))

# index = [pd.Timestamp('2000-01-01'),
#          pd.Timestamp('2000-01-02'),
#          pd.Timestamp('2000-01-03')]

# ts = pd.Series(np.random.rand(len(index)), index=index)
# print(ts)
# print()
# print(ts.index)

# index = pd.to_datetime(['2000-01-01', '2000-01-02', '2000-01-03'])
# ts = pd.Series(np.random.rand(len(index)), index=index)
# print(ts.index)

# Note: to understand the freq parameter, access to this link: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
print(pd.date_range(start='2022-06-01', periods=3, freq='H'))