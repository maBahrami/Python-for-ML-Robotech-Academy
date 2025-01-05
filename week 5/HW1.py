def diffCount(S1, S2):
    S1 = S1.lower()
    S2 = S2.lower()

    if len(S2) > len(S1):
        S3 = S1
        S1 = S2
        S2 = S3

    #print(f"S1 is {S1}")
    #print(f"S2 is {S2}")

    i = 0
    for k in range(len(S2)):
        if S1[k] != S2[k]:
            i += 1
    return i + (len(S1)-len(S2))


def findMismatch(S1, S2):
    S1 = S1.lower()
    S2 = S2.lower()

    if S1 == S2:
        print(0)
    else:
        n = diffCount(S1, S2)
        print(n)

        if len(S1) == len(S2) and n == 1:
            print(1)
        elif len(S1) != len(S2) or n >= 2:
            print(2)


"""
s1 = "helloothere"
s2 = "Hello There"
"""

"""

"""
s1 = 'Dogkl'
s2 = 'd G l'

findMismatch(s1, s2)

