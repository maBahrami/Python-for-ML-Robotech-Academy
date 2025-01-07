# tuple data structure is immutable
# tuple is faster than list

a = ('mammad', 3, 2, 5)

b = ([1, 2], 'mammad', (6, 9), 3, 2, 5)

a[0]

a[-1]

b[2][1]


type(('hi', ))

type(('hi'))


tuple([1, 2, 3])

list((1, 2, 3))


y = (1, 2, 3)
r, t, s = y         # tuple unpacking

# --------------------
def f(a, b):
    return a+b, a-b
output = f(3, 4)        # output = (7, -1)

sum, dif = f(3, 4)      # sum = 7   &   dif = -1
# --------------------

d = ('a', 'b', 'a', 'f', 'a')

print(d.count('a'))

print(d.index('b'))


for name in ("gholi", "sam"):
    print("Hello ", name)


# --------- some functions in tuple ---------------
a = (1, 6, 2, 9, 0, -2)
len(a)
max(a)
sum(a)
sorted(a)
min(a)
