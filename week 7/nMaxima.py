n = 3

a = [2, 9, 8, 5, 6, 7, 1, 10, 11, 12, 17, 5, 4, 16]

for _ in range(n):
    max = a[0]
    for i in a:
        if i > max:
            max = i
    a.remove(max)
    print(max, a)
