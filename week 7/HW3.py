import pandas as pd 

a = [100, 200, "python", 300.12, 400]

A = pd.Series(a)

B = pd.Series([500, "php"], index=[0, 1])

print(A)
print(B)

C = pd.concat([A, B])
print(C)

print(C[0])
print(C[1])