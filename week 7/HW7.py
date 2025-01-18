import pandas as pd

col1 = [1, 2, 3, 4, 5]
col2 = [2, 2, 2, 2, 2]
col3 = [3, 3, 0, 3, 3]

a = {'col1': col1, 'col2': col2, 'col3': col3}

df = pd.DataFrame(a)

print("----------------------------------")
print(df)
print("----------------------------------\n")

print("the average is:")
print(df.mean())
print("\nthe std is:")
print(df.std())
print("----------------------------------\n")

print((df - df.mean()) / df.std())