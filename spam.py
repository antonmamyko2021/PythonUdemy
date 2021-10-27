a = ['c','a', 'b','c']
b = ['d', 'f','c', 'k', 'c']


c = [a] + [b]


for index, value in enumerate(c):
    for i in range(len(value)-1,-1,-1):
        if value[i] == 'c':
            del value[i]
    print(list(value),end='')

