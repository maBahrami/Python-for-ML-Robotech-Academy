import numpy as np
import random

def printEnv(A):
    B = np.reshape(A, [3, 3])
    for i in B:
        print(f" {i[0]} | {i[1]} | {i[2]}")
        print("-----------")


def statusCheck(possibleMoves, environment):
    if len(possibleMoves) == 0:
        return "No Winner!"
    
    else:
        B = np.reshape(environment, [3, 3])
        ref_user = ['X', 'X', 'X']
        ref_pc = ['O', 'O', 'O']

        for i in B:
            if list(i) == ref_user:
                return "YOU ARE THE WINNER"
            elif list(i) == ref_pc:
                return "THE PC IS THE WINNER!"
        
        C = B . T
        for i in C:
            if list(i) == ref_user:
                return "YOU ARE THE WINNER"
            elif list(i) == ref_pc:
                return "THE PC IS THE WINNER!"
        
        diag = [B[0, 0], B[1, 1], B[2, 2]]
        if diag == ref_user:
            return "YOU ARE THE WINNER"
        elif diag == ref_pc:
            return "THE PC IS THE WINNER!"
        
        diag = [B[0, 2], B[1, 1], B[2, 0]]
        if diag == ref_user:
            return "YOU ARE THE WINNER"
        elif diag == ref_pc:
            return "THE PC IS THE WINNER!"

    return "OK"
    

env = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

printEnv(env)

status = "OK"
while status == "OK":
    status = statusCheck(possible, env)
    if status != "OK":
        break
    else:
        user = int(input(f"choose from {possible}.    "))
        env[user-1] = "X"
        possible.remove(user)
        printEnv(env)
        print("****************************")
    

    status = statusCheck(possible, env)
    if status != "OK":
        break
    else:
        pc = random.choices(possible)[0]
        env[pc-1] = "O"
        possible.remove(pc)
        printEnv(env)
        print("****************************")

print(status)