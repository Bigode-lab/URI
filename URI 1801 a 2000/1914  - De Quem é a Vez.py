#objetivo apresentar o jogador vencedor 
casos = int(input())
#quantidade de casos
for caso in range(casos):
    #enquanto caso for menor que casos
    jogador1, escolha1, jogador2, i = (str(x) for x in input().split())
    #leitura das escolas de cada jogador e seus nomes e armazenada 
    #em suas respectivas variaveis 
    a, b = (int(x) for x in input().split())
    #leitura de dois valores inteiros representado os valores colocados por cada jogador 
    r = (a+b)%2
    #calculo do resto da divisao da soma desses valores por 2
    if r == 0:
        #se o resto for 0 significa que a soma dos numeros resulta em um numero par
        if escolha1 == 'PAR':
            print(jogador1)
            #se a escolha do jogador 1 for par ele ganha
        else:
            #se nao ele perde
            print(jogador2)
    elif r != 0:
        #se o resto for 1 entao a soma dos numeros resulta e um numero impar
        if escolha1 == 'IMPAR':
            #se a escolha do jogador 1 for impar ele ganha
            print(jogador1)
        else:
            #se nao ele perde
            print(jogador2)