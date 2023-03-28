#objetivo calcular o conusmo de combustivel em uma viajem
tempo = int(input())
velocidade = int(input())
#leitura dos do tempo gasto e da velocidade media na viagem
combustivel = (tempo*velocidade)/12
#calculase a distancia e divide pelo consumo do caro que é 12km/l para obter a quantidade de combustivel gasto
print('{:.3f}'.format(combustivel))
#impressao do combustivel gasto