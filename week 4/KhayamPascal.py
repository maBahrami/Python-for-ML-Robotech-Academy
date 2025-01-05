a = [[1]]

n = int(input("enter the number of the rows"))

for i in range(1, n):
    x = [1, 1]
    for j in range(1, i):
        x.insert(j, a[i-1][j]+a[i-1][j-1])
    a.append(x)

for i in a:
    print(i)