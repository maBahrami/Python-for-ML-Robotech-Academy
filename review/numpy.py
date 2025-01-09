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







