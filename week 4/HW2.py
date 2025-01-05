def filter(a):
    b = []
    for i in a:
        if i != "":
            b.append(i)
    return b

l1 = [1, 2, "", " salam", "", "a"]

print(filter(l1))