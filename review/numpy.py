a = np.array([1, 2, 3])         # a is a 1*3 matrix

b = np.array([[1, 2, 3], 
              [4, 5, 6]])       # b is a 2*3 matrix


b[0][0]     # 1

b[0][2]     # 3

b[1][1]     # = 5


print(b.shape)          # (2, 3)
 

np.zeros((3, 4))

np.ones((2, 3), dtype = np.int16)


d = np.arange(10, 25, 5)        # (start, end, step)


e = np.linspace(0, 2, 10)       # (start, end, number of values)


f = np.full((2, 2), 7)          # a 2*2 matrix with all elements being 7


f = np.eye(2)                   # 2*2 identity matrix

g = np.random.random((2, 2))    # a 2*2 matrix with all elements being a random value between 0 and 1



# ------------------ save and load ------------------------------
np.save('myArray.npy', f)           # saving a single array

np.savez('myArray.npz', d, e)       # saving multiple arrays

np.load('myArray.npy')
# ---------------------------------------------------------------
np.load("myFile.txt")       # it is better to use pandas for this matter

#----------------------------------------------------------------

a.shape

len(a)

a.ndim

a.size

a.dtype

a.astype(int)

# --------------------- data types in numpy array ------------------------
a = np.array([1, 2, 3], dtype = int)      #int

a = np.array([1, 2, 3], dtype = float)    #float

a = np.array([1, 2, 3], dtype = complex)    # complex

a = np.array([1, 1, 0], dtype = bool)       # bool

# ------------------- mathematical operation in arrays -----------------
g = a - b

h = a + b

g = a / b  # each element is divided by the corresponfing element (it is not atrix multipilication)

g = a * b  


np.exp(a)       # exp() of each element will be calculated

np.sqrt(a)      # sqrt() of each element will be calculated

np.sin(a)       # sin() of each element will be calculated

np.cos(a)

np.log(a)



c = np.matmul(a, b)     # matrix multiplication

c = a @ b       # short form of the matrix multiplication



a == b          # elementwise arrays comparison

a < 2           # elementwise (a is an array)


np.sum(a, axis=0)
np.sum(a, axis=1)


# ---------------------- copying ----------------------------
a = np.array([1, 2, 3, 4, 5])

x = a.copy()

a[0] = 100      # just a willl be changed without affecting x

# ------------------------------------------------------------
a = np.array([[3, 6, 7, 1], [2, 6, 9, 4]])
b = np.sort(a, axis=0)
c = np.sort(a, axis=1)



# --------------- slicing ------------------------------

a = np.array([[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 3, 7, 9]])

b = a[0:2, 1:4]


b = a[::-1]  # reversing

c = a[low : high : stride]


# --------------- matrix transpose ----------------------

b = np.transpose(a)

b = a . T       # shorter form


# -------------- reshape --------------------------------
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

b = np.reshape(a, [3, 4])

c = np.reshape(a, [2, -1])      # 2 rows and undifinite number of columns


# ------------ concatenation -----------------------------
c = np.concatenate((a, b), axis=1)

c = np.hstack((a, b))

c = np.vstack((a, b))


# ------------ interesting example ---------------------
x = numpy.array([1,2,3,4]) #x
y = numpy.array([5,6,7])   #y 

x = x.reshape((-1,1))
                    '''    array([[1],
                                  [2],
                                  [3],
                                  [4]])           '''

diff_matrix = x-y
                    '''    array([[-4, -5, -6],
                                  [-3, -4, -5],
                                  [-2, -3, -4],
                                  [-1, -2, -3]])         '''