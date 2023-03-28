t = []
n = float(input())
for x in range(100):
    if x == 0:
        a = n
        t.append(a)
        print('N[{}] = {:.4f}'.format(x, t[x]))
    else:
        a = a/2
        t.append(a)
        print('N[{}] = {:.4f}'.format(x, t[x]))