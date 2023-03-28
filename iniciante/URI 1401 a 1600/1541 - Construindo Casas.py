#objetivo retornar o valor da medida de lado do terreno
n = [int(x)for x in input().split()]
#leitura de todos os valores inteiros por linha e armaenados em uma lista 
while n[0] != 0:
    #se o primeiro valor da lista for zero
    #essa condicao e colocada por que a ultima linha de entrada e um valor 0
    c = int(((n[0]*n[1]*100)/n[2])**0.5)
    #calculo da lateral do terreno
    print(c)
    #impressao do valor da lateral
    n = [int(x) for x in input().split()]
    #atualizacao da lista com novos valores para fazer o calculo de uma nova lateral do terreno 