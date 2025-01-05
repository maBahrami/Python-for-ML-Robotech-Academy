def f(a, b):
    output = []
    for i in a:
        for j in b:
            output. append(str(i)+" "+str(j))
    return output

l1 = ["Hello", "take"]
l2 = ["Dear", "Sir"]

print(f(l1, l2))