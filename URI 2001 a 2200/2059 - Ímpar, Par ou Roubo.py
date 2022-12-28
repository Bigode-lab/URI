escolha1, jogador1, jogador2, roubo, acusou = (int(x) for x in input().split())
resultado = (jogador1 + jogador2)%2
if roubo == 0:
    roubou = False
else:
    roubou = True

if acusou == 0:
    acusou = False
else:
    acusou = True

if (acusou and roubou):
    jogador = 2
elif acusou == roubou == False:
    if escolha1 != resultado:
        jogador = 1
    else:
        jogador = 2
else:
    jogador = 1

print(f'Jogador {jogador} ganha!')