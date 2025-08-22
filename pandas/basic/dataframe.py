import pandas as pd

data = {
  "height": [120, 180, 190],
  "weight": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
print("second row :  ", df.loc[1], sep = "\n")