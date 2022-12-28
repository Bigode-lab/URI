#mostrar quantos numeros sao positivos da entrada de 6 numeros e a sua media
positivos = 0
soma = 0
#inicaicao de 2 variaveis
for x in range(6):
    #enquanto x for menor que 6
    numero = float(input())
    #leitura de um numero de ponto flutuante
    if numero > 0:
        #se o numero for positivo
        soma += numero
        #somase o numero em soma
        positivos += 1
        #contase mais um nos positivos
print('{} valores positivos'.format(positivos))
#impressao da quantidade de numeros possitivos
media = soma / positivos
#calculo da media
print('{:.1f}'.format(media))
#impressao da media com uma casa decimal depois da virgula