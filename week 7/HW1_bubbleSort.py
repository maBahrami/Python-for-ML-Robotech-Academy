a = [1, 5, 0, 6, 8, 4, 8, 4, 4, 3, 2]

print(a)

j = 1
while j != 0:
    print("----------------------------------------")
    j = 0
    for i in range(0, len(a)-1):
        if a[i+1] < a[i]:
            a[i+1], a[i] = a[i], a[i+1]
            j += 1
        i += 1
        print(j, a)


print(a)

