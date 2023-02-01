#objetivo imprimir o nive de vvelocidade da lesma mais rapida do grupo de lesmas
#fim do arquivo se da por um EOF 
while True:
    try:
        n = int(input())
        #eitura de um inteiro n representandao a quantidade de lesmas por grupo
        lesmas = [int(x) for x in input().split()]
        #leitura das velociades das lemas de cada grupo e armazenandoas em uma lista 
        a = max(lesmas)
        #a recebe o  valor da lesma com maior velocidade
        if a < 10:
            print('1')
            #se o valor da maior velocidade for menor que 10 printamos que ela e do nivel 1
        elif a >= 20:
            print('3')
            #se o valor da maior velocidade for maior que 20 printamos que ela e do nivel 3
        else:
            print('2')
            #se nao ela e do nivel 2
    except EOFError:
        break