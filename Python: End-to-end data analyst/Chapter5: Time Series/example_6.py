from datetime import date
from ntpath import join
import pandas as pd
import re

directory = '/home/ducminh/Desktop/Academic_Study/Self-learning/Research/Dataset/Example/'
df = pd.read_csv(directory+'rbrted.csv')

df_date = df.Date 

def changeToComma(date_time):
    date_time = str(date_time)
    date_time = re.sub(',', '', date_time)
    date_time = re.sub('\s+', ',', date_time.strip())
    return date_time

# for i in range(0, len(df_date)):
#     df_date.iloc[i] = changeToComma(i)
    
# print(df_date.head(5))
# for i in range(0, len(df_date)):
#     df_date.iloc[i] = pd.to_datetime(df_date.iloc[i])
    
# print(df_date.head(5))

# df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# df2 = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]})
# df1.append(df2)
# print(pd.concat([df1, df2]))
# print(pd.concat([df1, df2], axis=1))
# print(pd.concat([df1, df2], keys=['UK', 'DE']))
# df3 = pd.concat([df1, df2], keys=['UK', 'DE'])
# print(df3)

# df1 = pd.DataFrame({"key": ['A', 'B', 'C', 'D'], 
#                     "value": range(4)})
# print(df1)
# print()
# df2 = pd.DataFrame({"key": ['B', 'D', 'D','E'], 
#                     "value": range(10, 14)})
# print(df2)
# print()

# print(df1.merge(df2, on='key'))
# print()
# # how= can be easily understood as some methods in SQL: 
#         # left: left outer join
#         # right: right outer join
#         # outer: full outer join
#         # inner: inner join
# print(df1.merge(df2, on='key', how='left'))
# print()
# print(df1.merge(df2, on='key', how='outer'))
# print()

print(df.head(5))