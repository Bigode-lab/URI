l = []
for x in range(10):
    a = int(input())
    if a > 0:
        l.append(a)
    else:
        a = 1
        l.append(a)
    print('X[{}] = {}'.format(x, l[x]))