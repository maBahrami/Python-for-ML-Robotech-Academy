a = [1, 1]

n = int(input("enter the number: "))

for i in range (2, n):
    a.append(a[i-2]+a[i-1])

print(a[:n])