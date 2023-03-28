#imprimir um numero lido invertido
numero = input()
#leitura do numero
for digito in range(len(numero)):
    #enquanto digito for menor do que a quantidade de digtos que o numero tem 
    print(f'{numero[-(digito+1)]}',end='')
    #impresao do ultimo digito sem quebra de lina um atras do outro imprimindo o numero inicial invertido
print('\n')
#impressao de uma quebra de linha para ficar no formato que o uri pede
