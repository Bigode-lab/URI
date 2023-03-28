cont = 0
t = int(input())
for x in range(t):
    a, b, g1, g2 = (float(x) for x in input().split())
    while a <= b:
        a = a + (a*g1//100)
        b = b + (b*g2//100)
        cont += 1
        if cont > 100:
            break
    if cont <= 100:
        print('{} anos.'.format(cont))
    else:
        print('Mais de 1 seculo.')
    cont = 0