import pandas as pd
import numpy as np

col1 = [1, 3, 2, 3, 2, 3, 1]
col2 = ["Ana", "Dima", "Kath", "James", "Emily", "Michael", "Matthew"]
col3 = [12.5, 9, 16.5, np.nan, 9, 20, 14]

a = {"a": col1, "b": col2, "c": col3}
print(a)

df = pd.DataFrame(a)
print(df)

df = df.fillna(0)
print(df)