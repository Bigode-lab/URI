n = int(input())
s = input()
l = []
t = []
for x in range(12):
    for y in range(12):
        a = float(input())
        l.append(a)
    if x == n:
        if s == 'S':
            print('{:.1f}'.format(sum(l)))
        elif s == 'M':
            print('{:.1f}'.format(sum(l)/12))
    t.append(l)
    l = []