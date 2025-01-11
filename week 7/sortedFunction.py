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

