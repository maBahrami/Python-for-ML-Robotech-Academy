import pandas as pd
'''
cities = {
            "A": 2,
            "B": 18,
            "C": 22,
            "D": 30
        }

temp = [2, 18, 22, 30]

# ------------------- Series -----------------------------
ct = pd.Series(cities)

t = pd.Series(temp)

t2 = pd.Series(temp, index = ["A", "B", "C", "D"])

print(ct.index)
print(ct.values)

# ------------------- element calling --------------------
print(ct["A"])
print(ct.A)
print(ct.iloc[0])

# ------------------- multi element calling -----------------
print(ct[["A", "B"]])
print(ct.iloc[[0, 3]])
print(ct[0:3])
print(ct["C":"D"])

print(ct[[True, False, False, True]])

# example
print(f"the mean temp is {ct.mean()}")
print(ct[ct >= ct.mean()])

'''
# ---------------------------- Data Frame --------------------------------------------
d = {"w":[60, 70, 80, 65], "h":[1.7, 1.8, 1.9, 1.3], "wrist":[12, 15, 18, 11]}

df = pd.DataFrame(d)
'''
print(df)

print(df.shape)

print(df.columns)

print(df.index)

print(df.values)

# ---------------- converting to numpy array -------------
import numpy as np
dataset = np.array(df.values)

# ---------------- head and tail preview ---------------------------------
print(df.head(2))

print(df.tail(2))

df.info()

print(df.describe())


# ------------------------- access to columns ------------------------
print(df["w"])

print(df.h)

print(df["h"] > 1.8)



# ----------------------  iloc method  ---------------------------
print(df)

print(df.iloc[0, 0])

print(df.iloc[1:, :2])

print(df.iloc[[0, 2], [0, 1]])

print(df.iloc[[True, False, True, False], ["w", "wrist"]])
'''

# ----------------------  loc method  ---------------------------
print(df)

print(df.loc[1, "w"])

print(df.loc[1:3, "w":"wrist"])

print(df.loc[[0, 2], ["w", "wrist"]])




