a = [9, 5, 5, 6, 5, 4, 7, 0]

for i in range(1, len(a)):
    key = a[i]
    j = i
    while key < a[j-1] and j != 0:
        a[j] = a[j-1]
        j -= 1
        print(a)
    a[j] = key

print(f"\n\nthe sorted list is: {a}\n\n")