# list data structure is mutable; pay attention when you want to copy a list or change some values

a = [1, 2, 3, 4, 5]
b = [1, 2, "mammad", "gholi"]   # any type
c = [1, 2, 3, [6, 5, 4], 9]     # nested list

a[0]
a[2:4]
a[:3]
a[:]
a[-1]
c[3][2]     # addressing in nested lists

a[3] = 56

n = len(a)

print(a + b)
print(b + c)

for i in a:
    print(i)

print("mammad" in b)        # true

print("mammad" not in b)     # flase


for index, item in enumerate(a):
    print(f"the index {index} is regarding to {item}")


# ------------ methods ------------
a = [1, 2, 3, 4, 5]
b = [1, 2, "mammad", "gholi"]   # any type
c = [1, 2, 3, [6, 5, 4], 9]

import copy
aa = copy.copy(a)
cc = copy.deepcopy(c)

b.index("mammad")

a.append(652)

a.insert(2, 2334)

b.remove("gholi")

a.sort()

a.sort(reverse = True)

a.reverse()

# paye careful attention to the fact that all of the methods do their function in plance


# ------------------------- sorted function -----------------------------------
def secondElement(i):
    return i[1]

a = [2, 9, 8, 5, 6, 7, 1, 10, 11, 12, 17, 5, ]
b = ['a', 'dv', 'absgf', 'w', 'wwr', 'ewerer']
c = [(1, 5), (5, 2), (6, 4), (3, 2), (8, 9)]

sortedArrayA = sorted(b, reverse = True)

sortedArrayB = sorted(b, key = len, reverse = True)

sortedArrayC = sorted(c, key = secondElement)

sortedArrayC2 = sorted(c, key = lambda i:i[1])      # using lambda instead of defining a seperate function



print(sortedArrayC2)

# --------------------------------------------------------------------------------


