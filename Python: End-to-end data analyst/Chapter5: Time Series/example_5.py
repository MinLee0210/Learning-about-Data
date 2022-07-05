# TIME SERIES PLOTTING
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rng = pd.date_range(start='2000', periods=120, freq='M')
ts = pd.Series(np.random.randint(-10, 10, size=len(rng)), rng).cumsum()
# print(rng)
# print(ts)

ts.plot(c='k', title='Example time series')
ts.resample('2A').plot(c='0.75', ls='--')
ts.resample('5A').plot(c='0.25', ls='-.')
plt.show()