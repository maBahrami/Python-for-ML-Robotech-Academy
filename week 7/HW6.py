import pandas as pd

col1 = [11, 14, 13, 14, 15]
col2 = [24, 25, 26, 27, 28]
col3 = [37, 38, 39, 30, 31]

a = {'col1': col1, 'col2': col2, 'col3': col3}

df = pd.DataFrame(a)

print(df)

df2 = df.reindex(columns = ['col3', 'col2', 'col1'])

print(df2)