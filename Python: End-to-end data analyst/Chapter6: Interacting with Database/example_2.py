# EXPORT DATA FROM THE DATA OBJECT TO A TEXT FILE

from operator import index
import pandas as pd 

directory = '/home/ducminh/Desktop/Academic_Study/Self-learning/Research/Dataset/Example/'

df = pd.read_csv(directory+'example_3', sep='\t', header=None, error_bad_lines=False)
print(df)

df.to_csv(directory+'example_out_3', sep=',')