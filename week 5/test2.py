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
        w = m
    else:
        w = i
    
    return w + (len(S1)-len(S2))


S1 = 'programing'
S2 = 'programming'

print(diffCount(S1, S2))