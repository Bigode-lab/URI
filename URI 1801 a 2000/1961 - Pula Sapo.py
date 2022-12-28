pulo, quantidade = (float(x) for x in input().split())
canos = [float(x) for x in input().split()]
f = False
cont = 0
for x in canos:
    if cont == 0:
        atual = x
        cont += 1
    else:
        r = abs(atual - x) > pulo
        if r :
            f = True
            break
        else:
            atual = x
if f:
    print('GAME OVER')
else:
    print('YOU WIN')