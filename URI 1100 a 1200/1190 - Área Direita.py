c = []
l = []
cont  = 0
a = 11
soma = 0
s = input()
for x in range(12):
    for y in range(12):
        n = float(input())
        if y > a:
            soma += n
            cont += 1
        l.append(n)
    c.append(l)
    l = []
    if len(c)<= 5:
        a -= 1
    elif len(c) < 6:
        a += 1 
    


if s == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/cont))

