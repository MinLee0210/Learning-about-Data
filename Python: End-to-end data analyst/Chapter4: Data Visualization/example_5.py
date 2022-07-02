# PLOTTING FUNCTIONS WITH PANDAS

from operator import index
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# s = pd.Series(np.random.normal(10, 8, 20))
# s.plot(style='ko-', alpha=0.4, label='Series plotting')
# plt.legend()
# plt.show()

data = {'Median_Age': [24.2, 26.4, 28.5, 30.3], 
        'Density': [244, 256, 268, 279]}
index_label = ['2000', '2005', '2010', '2014']
df1 = pd.DataFrame(data, index=index_label)
df1.plot(kind='bar', subplots=True, sharex=True)
plt.tight_layout()
plt.show()