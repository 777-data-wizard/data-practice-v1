import pandas as pd
df = pd.read_csv('titanic.csv')
print(df.head()) 
print(df.loc[range(0, 7)])
print(df)