import pandas as pd

pd.options.display.max_rows = 9999999
df = pd.read_csv('titanic.csv')
print(df)