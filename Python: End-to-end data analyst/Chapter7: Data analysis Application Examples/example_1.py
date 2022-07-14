import pandas as pd
import datetime
import numpy as np

directory = '/home/ducminh/Desktop/Academic_Study/Self-learning/Research/Dataset/Example/'

# df = df.rename(columns={'Europe Brent Spot Price FOB (Dollars per Barrel)': 'Price'})
def convert_date(s):
    parts = s.replace("(", "").replace(")", "").split(",")
    if len(parts) < 6:
        return datetime.date(1970, 1, 1)
    return datetime.datetime(*[int(p) for p in parts])
df = pd.read_csv(directory+'rbrted.csv', sep=',', names=["date", "price"],
                        converters={"date": convert_date}).dropna()

print(df)
# print(df[df['Price'] == df['Price'].min()])
# print()
# print(df[df['Price'] == df['Price'].max()])
# print()
# Calculate the deviation from the mean
# print(np.abs(df.Price - df.Price.mean()))
# print()
# Compare deviation to the standard deviation, we will do some algorithmetic operations as an example
# print(df[df.Price - df.Price.mean() > 2.5*df.Price.std()])
# print()
