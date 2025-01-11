a = [9, 5, 5, 6, 5, 4, 7, 0]

for i in range(1, len(a)):
    j = i - 1 
    mem = a[i]
    while (mem < a[j]) and (j > -1):
        a[j+1] = a[j]
        print(a)
        j -= 1
    a[j + 1] = mem
    
    print(f"---------{a}-----")
