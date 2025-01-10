import matplotlib.pyplot as plt

data = {"Java": 22.2, "Python": 17.6, "PHP": 8.8, "JavaScript": 8, "C#": 7.7, "C++": 6.7}

x = list(data.values())
y = (list(data.keys()))
print(x)
print(y)

plt.bar(y, x)


plt.show()