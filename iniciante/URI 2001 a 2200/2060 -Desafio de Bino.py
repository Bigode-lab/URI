dois = 0
cinco = 0
tres = 0
quatro = 0
#iniciacao das variaveis inteiras
n = int(input())
#leitura da quantidade de numeros 
numeros = [int(x) for x in input().split()]
#leitura dos numeros e armazenandos em uma lista
for x in numeros:
#percorrendo aista
    if x%2 == 0:
        dois += 1
        #se x for divisivel por 2 adicionamos 1 a variavel
    if x%3 == 0:
        tres += 1
        #se x for divisivel por 3 adicionamos 1 a tres
    if x%4 == 0:
        quatro += 1
        #se x for divisivel por 4 adicionamos 1 a quatro
    if x%5 == 0:
        cinco += 1
        #se x for divisivel por 5 adicionamos 1 a cindo
print(f'{dois} Multiplo(s) de 2\n{tres} Multiplo(s) de 3\n{quatro} Multiplo(s) de 4\n{cinco} Multiplo(s) de 5')
#impressao da quantidade de numeros divisiveis por 2, 3, 4 e 5 na lista
