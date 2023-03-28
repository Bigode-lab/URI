#dado um numero de casos, calcular em cada caso a media ponderada de 3 notas
casos = int(input())
#leitura de um numero inteiro que sera o numerod e casos
for x in range (casos):
    #enquanto x for menor que casos
    nota1, nota2, nota3 = (float(x) for x in input().split(' '))
    #leitura de cada uma das notas
    pesos = (nota1 * 2) + (nota2*3) + (nota3*5)
    #pesos recebe a soma de cada uma das notas vezes o seu respectivos pesos
    media = pesos/10
    #calculo da media ponderada
    print(f'{pesos:.1f}')
    #impressao da media com uma casa decimal apos a virgula