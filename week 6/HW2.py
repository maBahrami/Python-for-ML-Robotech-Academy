import numpy as np
import matplotlib.pyplot as plt

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



print("\n---------- part j ---------------------")


print("\n---------- part k ---------------------")