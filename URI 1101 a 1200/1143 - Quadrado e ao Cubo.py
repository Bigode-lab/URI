#objetino printar  n linhas q=com as eguinda saida x, o quadraddo de x e o cubo de x
n = int(input())
#leitura de um numero inteiro
for x in range(n):
    #enquanto x for menor que n
    print('{} {} {}'.format((x+1), ((x+1)**2), ((x+1)**3)))
    #impressao da saida
    #como x inicia em 0 por isso somase +1 a x para iniciar em 1 na saida