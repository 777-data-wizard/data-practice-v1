import pandas as pd
from math import floor

df = pd.read_csv('test2.csv')
df["Birthday"] = pd.to_datetime(df["Birthday"], format=None)
print(df.info())
print(df.head())