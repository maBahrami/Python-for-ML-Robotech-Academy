a = [1, 2, 3, ["a", "b"], 987]
b = [1, 2, 3]

for i in b:
    print(i)
    b.append(i)
    print(b)