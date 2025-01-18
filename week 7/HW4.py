import pandas as pd

a = [["red", "green", "white"], ["red", "black"], ["yellow"]]
A = pd.Series(a)

print(A)


B = pd.Series([])
print(B)

print("--------------")
for i in A.values:
    B = pd.concat([B, pd.Series(i)], ignore_index=True)

print(B)

