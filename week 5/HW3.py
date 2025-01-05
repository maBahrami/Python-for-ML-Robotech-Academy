import copy

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
    #print(f"the i is {i}")

    m = 0
    for l in range(-1, -len(S2)-1, -1):
        if S1[l] != S2[l]:
            m += 1 
    #print(f"the m is {m}")

    if i >= m:
        w = m
    else:
        w = i
    
    return w + (len(S1)-len(S2))



#input = 'Thes is the First cas'
#dictionary = ['that', 'first', 'case', 'car']

#input = 'programing is fan and eesy'
#dictionary = ['programming', 'this', 'fun', 'easy', 'book']

#input = 'Thes is vary essy'
#dictionary = ['this', 'is', 'very', 'very', 'easy']

input = 'Wee ipve Pythen'
dictionary = ['we', 'Live', 'In', 'Python']

inputList = input.lower().split()

a = []
for i in dictionary:
    a.append(i.lower()) 
dictionary = copy.copy(a)


output = []

for i in inputList:
    flag = False
    if len(i) <= 2:
        output.append(i)
    else:
        if i in dictionary:
            output.append(i)
        else:
            for j in dictionary:
                n = diffCount(i, j)
                print(i , j, n)

                if n <= 1:
                    output.append(j)
                    flag = True
                    break
            if flag == False:
                output.append(i)


print(f'the input sentence is: {inputList}')
print(f'the dictionary is: {dictionary}')


print()
print(output)
