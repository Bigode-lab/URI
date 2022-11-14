a = [int(x) for x in input().split(' ')]
n = (a[0]*60) + a[1]
n1 = (a[2]*60) + a[3]
t = n1 - n
if t <=0:
    t = t + (24*60)
b = t//60
c = t%60
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(b, c))