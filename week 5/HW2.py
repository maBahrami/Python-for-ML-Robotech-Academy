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
    print(f"the i is {i}")

    m = 0
    for l in range(-1, -len(S2)-1, -1):
        if S1[l] != S2[l]:
            m += 1 
    print(f"the m is {m}")

    if i >= m:
        output = m
    else:
        output = i
    
    return output + (len(S1)-len(S2))


def singleInsertOrDelete(S1, S2):
    S1 = S1.lower()
    S2 = S2.lower()

    if S1 == S2:
        print(0)
    elif len(S1) == len(S2):
        print(2 )
    else:
        p = diffCount(S1, S2)
        print(f"the diff counter is {p}")
        if p == 1:
            print(1)
        else:
            print(2)



s1 = 'pome'
s2 = 'poke'

singleInsertOrDelete(s1, s2)

