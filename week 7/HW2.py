import pandas as pd

a = [2, 4, 6, 8, 10]
b = [1, 3, 5, 7, 10]

A = pd.Series(a)
B = pd.Series(b)

print(A.values <= B.values)
