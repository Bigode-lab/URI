#bjetivo calcular a duraçãod e um jogo
a = [int(x) for x in input().split(' ')]
#leitura de 4 numeros inteiros representando as hora inicial e final do jogo
n = (a[0]*60) + a[1]
n1 = (a[2]*60) + a[3]
#transformação das horas em minutos
t = n1 - n
#calculo da duracao do jogo
if t <=0:
    t = t + (24*60)
#se o calculo der negativo soma-se mais 24 horas pq foi mais de um dia ou quase um dia 
b = t//60
c = t%60
#tranformacao no formato hh/mm
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(b, c))
#impressao