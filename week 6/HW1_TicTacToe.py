import numpy as np
import random

def printEnv(A):
    B = np.reshape(A, [3, 3])
    for i in B:
        print(f" {i[0]} | {i[1]} | {i[2]}")
        print("-----------")

env = [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

printEnv(env)

status = "OK"
while status == "OK":
    user = int(input(f"choose from {possible}.    "))
    env[user-1] = "X"
    possible.remove(user)

    printEnv(env)

    pc = 
