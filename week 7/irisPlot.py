import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv(r"week 7\dataset\iris.csv")

label = df["variety"]
print(label)
classes =label.value_counts()
print(classes)

plt.subplot(2, 2, 1)
plt.bar(classes.index, classes.values)
plt.xlabel("variety")
plt.ylabel("frequency")




sl = df.iloc[:, 0]
sw = df.iloc[:, 1]

pl = df.iloc[:, 2]
pw = df.iloc[:, 3]


plt.subplot(2, 2, 2)
plt.scatter(pl.index, pl, c = list("r"*50 + "g"*50 + "b"*50))
plt.xlabel("index")
plt.ylabel("petal length")


sepal = df.iloc[:50, 0]

plt.subplot(2, 2, 3)
plt.hist(sepal)
plt.xlabel("sepal length of Setosa")
plt.ylabel("f")

plt.subplot(2, 2, 4)
plt.scatter(sl, sw, c = list("r"*50 + "g"*50 + "b"*50))
plt.xlabel("sepal length")
plt.ylabel("sepal width")


plt.show()



