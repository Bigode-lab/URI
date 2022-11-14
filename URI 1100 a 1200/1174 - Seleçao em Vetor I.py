t = []
for y in range(100):
    a = float(input())
    t.append(a)
    if a <= 10:
        print('A[{}] = {}'.format(y, t[y]))