def area(a, b, step):
    A = 0
    while(a < b):
        A += (a*a) * step
        a += step
    return(A)

a = -2
b = 2
step = 0.001

print(area(a, b, step))