escolha1, jogador1, jogador2, roubo, acusou = (int(x) for x in input().split())
#leitura da escolha do jogador 1 e o numero jogado, numero jogado pelo jogador 2, se o jogador 1 roubou e se o jogador 2 acusou ou nao
resultado = (jogador1 + jogador2)%2
#verificandao se a soma das escolhas dos jogadores e impar ou par
if roubo == 0:
    roubou = False
else:
    roubou = True
#verificando se o jogador 1 roubou ou nao e convertendo isso para um valor booleano

if acusou == 0:
    acusou = False
else:
    acusou = True

#verificando se o jogador 2 acusou ou nao e convertendo isso para um valor booleano
if (acusou and roubou):
    jogador = 2
    #se o jogador 1 roubou e o 2 acusou o jogador 2 ganha
elif acusou == roubou == False:
#se o jogador 1 nao roubou e o jogador 2 nao acusou o roubo
    if escolha1 != resultado:
    #se a escolha do jogador 1 for diferente do resultado
        jogador = 1
        #jogador 1 cvence
    else:
        jogador = 2
        #se nao jogador 2 vence
else:
    jogador = 1
    #em qualquer outro caso o 1 ganha

print(f'Jogador {jogador} ganha!')
#impressao do vencedor
