# import copy

def DLcounter(i, j, matrix):
    alive = 0
    if(matrix[j-1][i-1] == 1):
        alive += 1
    if(matrix[j][i-1] == 1):
        alive += 1
    if(matrix[j+1][i-1] == 1):
        alive += 1
    if(matrix[j-1][i] == 1):
        alive += 1
    if(matrix[j+1][i] == 1):
        alive += 1
    if(matrix[j-1][i+1] == 1):
        alive += 1
    if(matrix[j][i+1] == 1):
        alive += 1
    if(matrix[j+1][i+1] == 1):
        alive += 1


    if matrix[j][i] == 1:
        if alive == 2 or alive == 3:
            output = 1
        else:
            output = 0
    

    elif matrix[j][i] == 0:
        if alive == 3:
            output = 1
        else:
            output = 0

    return output


step = 5


# constructing the environment matrix A with all cells dead
# due to the referencing and the intention of not using deepcopy() this manner has been followed
n = 10 # number of rows and columns
A = []
for _ in range(0, n):
    x = [0]
    for _ in range(1, n):
        x.append(0)
    A.append(x)

#print(A)

# initial condition (asking for alive cells)
print("let's detrmine the alive cells")
condition = int(input("continue? "))
while (condition != 0):
    i = int(input("enter the i of the alive cell: "))
    j = int(input("enter the j of the alive cell: "))

    A[j][i] = 1
    condition = int(input("continue? "))



for s in range(step):
    print("The result of the step ", s, "is:")
    print()

    #backuping A
    previousA = []
    for i in A:
        previousA.append((list(i)))
    
    # or simply:
    # previousA = copy.deepcopy(A)
    
    for k in A:
        print(k)
    print("----------------------------------------------------------")
    print()
    
    for j in range(1, n-1):
        for i in range(1, n-1):
            status = DLcounter(i, j, previousA)
            A[j][i] = status
