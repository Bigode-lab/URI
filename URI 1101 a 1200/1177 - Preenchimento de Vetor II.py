n = int(input())
m = n-1
a = m
t = []
for x in range(1000):
    if  a == m:
        a = 0
        t.append(a)
        print('N[{}] = {}'.format(x, t[x]))
    else:
        a += 1
        t.append(a)
        print('N[{}] = {}'.format(x, t[x]))