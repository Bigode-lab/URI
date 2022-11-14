c = []
l = []
cont  = 0
a = 4
b = 7
soma = 0
s = input()
for x in range(12):
    for y in range(12):
        n = float(input())
        if (len(c) > 6) and (( y > a) and (y < b)):
            soma += n
            cont += 1
        l.append(n)
    c.append(l)
    l = []
    if (len(c) > 7):
        a -= 1
        b += 1

if s == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/cont))

