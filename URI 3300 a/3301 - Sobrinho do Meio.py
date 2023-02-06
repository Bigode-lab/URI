meninos = [int(x) for x in input().split()]
#lendo as idades dos meninos e armazenando em ma lista, onde cada indice se refere a os meninos certinho
maior = max(meninos)
#identificadno o subrinho mais velho
menor = min(meninos)
#identificando o subrino mais novo
for x in range(3):
    #percorendo a lista do meninos pelos indices
    if meninos[x] != menor and meninos[x] != maior:
        #identificando o subrinho mais novo 
        index = x
        #retornando o indice para identificar o mais novo
if index == 0:
    print('huguinho')
elif index == 1:
    print('zezinho')
elif index == 2:
    print('luisinho')
#imprimindo o subrino mais novo