import pandas as pd
a = [1, 7, 2, 10]
myvar = pd.Series(a, index = ["a", "b", "c", "d"])
print("myvar[0]: ", myvar[0])
print("myvar['b']:", myvar['b'])
print(myvar)