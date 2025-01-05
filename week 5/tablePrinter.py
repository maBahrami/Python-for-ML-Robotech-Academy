import numpy as np

a = [['apples', 'oranges', 'cherries', 'banana'],
     ['Alice', 'Bob', 'Carol', 'David'],
     ['dogs', 'cats', 'moose', 'goose']]



lenA = []
for i in a:
    k = []
    for j in i:
        k.append(len(j))
    lenA.append(k)


lenA = np.array(lenA)

maxEachColumn = np.max(lenA, axis=0)


B = []
for i in a:
    p = 0
    k = []
    for j in i:
        #print(j)
        out = ""
        n = maxEachColumn[p] - len(j)
        for _ in range(n):
            out += " "
        out += j
        k.append(out)
        p += 1
    
    B.append(k)
    print(k)



for i in B:
    for j in i:
        print(j, end='\t')
    print()