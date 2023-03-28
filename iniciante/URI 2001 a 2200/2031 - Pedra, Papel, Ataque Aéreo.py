casos = int(input())
#leitura da quantidade de casos de repeticao
for x in range(n):
#enquanto x for menor que n
    jogador1 = input()
    jogador2 = input()
    #leitura das respostas dos jogadores
    if jogador1 == jogador2:
        if jogador1 == 'pedra':
            print('Sem ganhador')
        elif jogador1 == 'papel':
            print('Ambos venceram')
        elif jogador1 == 'ataque':
            print('Aniquilacao mutua')
    elif jogador1 == 'ataque':
        print('Jogador 1 venceu')
    elif jogador2 == 'ataque':
        print('Jogador 2 venceu')
    elif jogador1 == 'pedra' and jogador2 == 'papel':
        print('Jogador 1 venceu')
    elif jogador2 == 'pedra' and jogador1 == 'papel':
        print('Jogador 2 venceu')
    #casos das possibilidades dos jogadores e impressao do vencedor
