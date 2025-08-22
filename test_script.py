import pandas as pd

mydataset = {
  'cars': ["LEXUS", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
