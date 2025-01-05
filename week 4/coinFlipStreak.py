import copy
import random

# a = [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]

def count(a):
    counter = 0
    b = copy.copy(a)

    b.insert(0, not a[0])
    b.append(not a[-1])

    #print(b)

    for i in range(1, len(a)-4):
        if b[i] != b[i-1] and b[i] == b[i+1] and b[i] == b[i+2] and b[i] == b[i+3] and b[i] == b[i+4] and b[i] == b[i+5] and b[i] != b[i+6]:
            counter += 1
            #print("the index is:", i)
    return counter

streaks = 0
for _ in range(10000):
    A = []
    for _ in range(100):
        A.append(random.randint(0, 1))
    num = count(A)
    #print(num)
    streaks += num
print(streaks)
