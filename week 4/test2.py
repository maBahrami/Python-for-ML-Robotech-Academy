a = (1, 2, 3, ["a", "b"])
print(a)

print(a[3])

a[3][0] = "c"

print(a)

def f(a, b):
    return a+b, a-b

output = f(3, 5)
print(output)
print(type(output))

c, d = f(8, 9)

print(c)
print(d)