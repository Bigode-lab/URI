j = True
i = 0
g = 0
e = 0
cont = 1
while j:
    a, b = (int(x) for x in input().split(' '))
    if a > b:
        i += 1
    elif b > a:
        g += 1
    else:
        e += 1
    c = int(input('Novo grenal (1-sim 2-nao)\n'))
    if c == 1:
        cont += 1
    elif c == 2:
        j = False
print('{} grenais'.format(cont))
print('Inter:{}'.format(i))
print('Gremio:{}'.format(g))
print('Empates:{}'.format(e))
if i > g:
    print('Inter venceu mais')
elif g> i:
    print('Gremio venceu mais')
else:
    print("Nao houve vencedor")