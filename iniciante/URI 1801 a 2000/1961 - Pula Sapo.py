#obejtivo imprimir se o jogador ganhou ou naão
pulo, quantidade = (float(x) for x in input().split())
#leitura de dois valores de ponto flutuante a altura do pulo do sapo
#e a quantidade de canos que ele tem q pular
canos = [float(x) for x in input().split()]
#leitura das alturas dos canos e armazenando em uma lista
sentinela = False
#iniciando uma variavel sentinela usada para saber se o jogador perdeu 
cont = 0
#ciniciando um contador
for cano in canos:
    #percorendo a lista cano vai ter a altura do cano respectivo
    if cont == 0:
        atual = cano
        cont += 1
        #se o contador e 0 entao e o primeiro cano que e de onde o sapinho inicia 
        #logo ele e o cano atual que o sapinho esta
        #e o contador soma mais um pois no proximo cano ja sera o segundo 
    else:
        #se o cano for do segundo endiante
        if abs(atual - x) > pulo:
            #tomamos o valor absoluto da diferenca entre os canos e vemos se e maior que o pulo
            #pois se for muito alto o sapino morre de queda e se for muito baixo ele nao alcanca o cano
            sentinela = True
            #se o valor for maior que o pulo entao o jogador pedeu ai atribimos um valor verdadeio
            break
            #a variavel sentinela e saimos do laço for 
        else:
            atual = cano
            #se o sapo conseguir alcancar o cano passa a ser o cano atual
if sentinela:
    print('GAME OVER')
    #se o jogador perder imprimimos game over
else:
    print('YOU WIN')
    #se o jogadorganar imprimmimos ou win