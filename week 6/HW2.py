import numpy as np
import matplotlib.pyplot as plt
'''
print("\n---------- part a ---------------------")
A = np.reshape(np.arange(0, 9), [3, 3])
print(A)

print("\n---------- part b ---------------------")
B = np.random.random((3, 3))
print(B)

print("\n---------- part c ---------------------")
C = np.random.random((10, 10))
print(f"the maximum of C is {float(C.max())}")
print(f"the minimum of C is {float(C.min())}")

print("\n---------- part d ---------------------")
D1 = np.arange(0, 5)
D = np.zeros((5, 5))
for i in range(len(D)):
    D[i] = D1
print(D)

print("\n---------- part e ---------------------")
E1 = np.random.random((3, 3))
E2 = np.random.random((3, 3))
print(E1 == E2)

print("\n---------- part f ---------------------")



print("\n---------- part g ---------------------")
G = np.random.random((2, 2, 2))
print(G)
for index, x in np.ndenumerate(G):
    print(index, x)


print("\n---------- part h ---------------------")
H1 = np.array([[1, 2],
               [3, 4]])
H2 = H1[::-1]
print(H1)
print()
print(H2)

print("\n---------- part i ---------------------")
I = np.reshape(np.arange(0, 256), [16, 16])
print(I)
for i in range(0, 13):
    for j in range(0, 13):
        I2 = I[i:i+4, j:j+4]
        #print(I2)
        print(I2.sum())


print("\n---------- part j ---------------------")
J = np.zeros((5, 5))
for i in range(5):
    J[i] = np.random.randint(low = 0, high = 4, size = 5)
print(J)
print(max)


print("\n---------- part k ---------------------")
k = np.random.randint(low = 0, high = 24, size = 25)
K = np.reshape(k, [5, 5])
print(K)
n = int(input("enter k: "))
q = 0
for i in K:
    print(f"the {n} maxima of the {q}th row are: ", end="\t")
    for j in range(n):
        i = list(i)
        m = max(i)
        print(f"{m}", end="\t")
        i.remove(m)
    print()
    q += 1

'''

print("\n---------- part l ---------------------")
x = np.array([1, 2, 3])
y = np.array([4, 8, 9, 7])

x = x.reshape((-1, 1))

diff = x - y
cauchy = 1.0 / diff

print(cauchy)