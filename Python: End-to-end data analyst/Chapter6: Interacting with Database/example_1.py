# LOAD DATA FROM TEXT FILE
import pandas as pd
import csv

directory = '/home/ducminh/Desktop/Academic_Study/Self-learning/Research/Dataset/Example/'
df_ex1 = pd.read_csv(directory+'example_1')

f = open(directory+'example_3')
r = csv.reader(f, delimiter='\t')
for line in r:
    print(line)