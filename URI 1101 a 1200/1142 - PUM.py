#objetivo imprimir n vezes uma saida que segue o padrao de acrecimo de 4 em a , b e c
a = 1
b = 2
c = 3
#iniciando as variaveis a, b e c
n = int(input())
#leitura de um numero n
for x in range(n):
    #enquanto x for menor que n
    print('{} {} {} PUM'.format(a, b, c))
    #impressao de a, b e c
    a += 4
    b += 4
    c += 4
    #imcrementacao de a, b e c em +1