#idenntificar quantos numeros possitivos se encontra em 6 entradas
positivo = 0
#inicialcao da variavel possitivos
for x in range(6):
    #enquanto x for menor que 6
    numero = float((input()))
    #leitura de um numero inteiro
    if numero >= 0:
        #analisando se ele e possitivo
        positivo += 1
        #implementando o contador de numeros positivos
print('{} valores positivos'.format(positivo))
#impressao da quantidade de numeros positivos