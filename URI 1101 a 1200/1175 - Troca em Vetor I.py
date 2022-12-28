t = []
for x in range(20):
    n = int(input())
    t.append(n)
for y in range(10):
    a = t[y]
    b = t[-(y+1)]
    t[-(y+1)] = a
    t[y] = b
for z in range(20):
    print('N[{}] = {}'.format(z, t[z]))