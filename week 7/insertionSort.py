a = [9, 5, 5, 6, 5, 4, 7, 0]

for i in range(1, len(a)):
    flag = True
    k = i
    j = k - 1
    print(i, k, j)
    while (flag == True) and (j > -1):
        if a[k] < a[j]:
            mem = a[j]
            a[j] = a[k]
            a[k] = mem

            k -= 1
            j = k -1 
            print(a)
        else:
            flag = False

print("\n---------------- * Finito * --------------------\n")
print(a)
