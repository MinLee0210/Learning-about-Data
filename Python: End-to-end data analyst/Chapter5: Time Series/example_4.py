import pandas as pd
import numpy as np
import pytz 
# pytz is a library for messing with timzone

# t = pd.Timestamp('2000-01-01', tz='Europe/Berlin')
# # print(t.tz is None)

# rng = pd.date_range('1/1/2000 00:00', periods=10, freq='D', 
#                     tz='Europe/Berlin')

tz= pytz.timezone('Europe/Berlin')
rng=pd.date_range('1/1/2000 00:00', periods=10, freq='D', tz=tz)

print(rng)

# NOT DONE YET