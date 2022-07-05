# RESAMPLING, DOWNSAMPLING, UPSAMPLING

import pandas as pd
import numpy as np

# RESAMPLING: the process of frequency conversion over time series data.
#             Improve the understanding via grouping and aggregrating data.
#             2 main features: bining-aggregration and filling in missing data. 

# DOWNSAMPLING: reduce the number of samples in the data

rng = pd.date_range('4/29/2015 8:00', periods=600, freq='T')
ts = pd.Series(np.random.randint(0, 100, len(rng)), index=rng)
print(ts.head(5))
print()
print(ts.resample('10min'))

# NOT DONE YET