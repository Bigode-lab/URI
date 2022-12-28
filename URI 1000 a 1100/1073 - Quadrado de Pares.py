#imprimir o quadrado de cada numero par no intervalo de 1 ate n
contador = 2
#inicio da sequencia
n = int(input())
#leitura do numero fim do intervalo
while contador <= n:
    #enquanto o contador for menor que n
    a = contador*contador
    #a recebe o quadrado do contador
    print('{}^2 = {}'.format(contador, a))
    #impressao do numero atua da sequencia de pares ate n
    #e de seu quadrado
    contador += 2
    #contador atribuido em +2
    #chegando ao proximo numero par