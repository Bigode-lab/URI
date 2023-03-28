n = int(input())
for x in range(n):
    z = int(input())
    cont = 1
    div = 0
    while cont <= z or div <2:
        a = z%cont
        if a == 0:
            div += 1
        cont += 1
    if div == 2:
        print('{} eh primo'.format(z))
    else:
        print('{} nao eh primo'.format(z))