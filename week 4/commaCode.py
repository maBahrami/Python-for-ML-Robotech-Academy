def comma(x):
    message = ''
    for i in x:
        if i == '':
            x.remove(i)

    if len(x) != 0:
        for i in x[:-1]:
            message += str(i)
            message += ', '
        
        message += 'and '
        message += str(x[-1])

        print(message)
    else:
        print("The list is empty")


n = ['apple', '', 'banana', '', 'tofu', 6, 'cat']
# n = []

comma(n)